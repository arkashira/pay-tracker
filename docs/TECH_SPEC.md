# TECH_SPEC.md – Pay‑Tracker

---

## 1. Overview

**Pay‑Tracker** is a lightweight, cloud‑native billing & invoicing platform designed for developers and small‑to‑mid sized businesses.  
It exposes a REST/GraphQL API for creating invoices, recording payments, and generating status reports.  
The system is built on Axentx’s proven stack (Python, FastAPI, PostgreSQL, Redis, Docker) and follows the company’s “self‑improving” data‑driven workflow: all user actions are logged, paired with feedback, and fed back into the training pipeline.

---

## 2. Architecture

```
┌──────────────────────┐
│   External Clients   │
│  (Web, Mobile, API)  │
└─────────────┬────────┘
              │
              ▼
┌──────────────────────┐
│   API Gateway (NGINX)│
└───────┬───────────────┘
        │
        ▼
┌──────────────────────┐
│  FastAPI Service      │
│  (paytracker.api)     │
│  • REST & GraphQL     │
│  • Auth (JWT)         │
│  • Rate limiting      │
└───────┬───────────────┘
        │
        ▼
┌──────────────────────┐
│  Domain Layer        │
│  (paytracker.core)   │
│  • Invoice, Payment   │
│  • Status Engine      │
│  • Collection Rules   │
└───────┬───────────────┘
        │
        ▼
┌──────────────────────┐
│  Persistence Layer   │
│  (paytracker.db)     │
│  • PostgreSQL        │
│  • SQLAlchemy ORM    │
│  • Alembic migrations│
└───────┬───────────────┘
        │
        ▼
┌──────────────────────┐
│  Cache & Queue       │
│  • Redis (caching)   │
│  • RQ (background jobs)│
└───────┬───────────────┘
        │
        ▼
┌──────────────────────┐
│  External Services   │
│  • Email (SendGrid)  │
│  • SMS (Twilio)      │
│  • Payment Gateways  │
└──────────────────────┘
```

### 2.1 Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Domain‑Driven Design** | Core business logic isolated in `core` package. |
| **Event‑Sourcing for Audits** | Every state change emits a domain event stored in `events` table. |
| **Self‑Improving Loop** | All events are paired with user feedback and pushed to the `auto` dataset for future model training. |
| **Stateless API** | Enables horizontal scaling behind NGINX. |
| **Observability** | Prometheus metrics, OpenTelemetry tracing, structured logs. |

---

## 3. Data Model

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `users` | Auth & billing accounts | `id`, `email`, `hashed_pw`, `role`, `created_at` |
| `invoices` | Invoice records | `id`, `user_id`, `amount`, `due_date`, `status`, `created_at`, `updated_at` |
| `payments` | Payment transactions | `id`, `invoice_id`, `amount`, `method`, `status`, `transaction_id`, `created_at` |
| `events` | Domain events for audit & training | `id`, `entity_type`, `entity_id`, `event_type`, `payload`, `created_at` |
| `feedback` | User feedback on events | `id`, `event_id`, `feedback_type`, `comment`, `created_at` |

### Status Engine

- **Invoice Status**: `draft`, `sent`, `paid`, `overdue`, `cancelled`
- **Payment Status**: `pending`, `completed`, `failed`

The status engine is a deterministic state machine implemented in `core/status.py`. It reacts to `PaymentCreated`, `PaymentCompleted`, `InvoiceSent` events.

---

## 4. Key APIs / Interfaces

| Endpoint | Method | Description | Request | Response |
|----------|--------|-------------|---------|----------|
| `/api/v1/invoices` | POST | Create invoice | `{"user_id": int, "amount": float, "due_date": str}` | `201 Created` + invoice JSON |
| `/api/v1/invoices/{id}` | GET | Retrieve invoice | N/A | Invoice JSON |
| `/api/v1/invoices/{id}/pay` | POST | Record payment | `{"amount": float, "method": str}` | `202 Accepted` |
| `/api/v1/invoices/{id}/status` | GET | Current status | N/A | `{ "status": str, "next_action": str }` |
| `/api/v1/collections` | GET | List overdue invoices | Query params: `page`, `size`, `sort` | Paginated list |
| `/api/v1/feedback` | POST | Submit feedback on event | `{"event_id": int, "feedback_type": str, "comment": str}` | `201 Created` |

### GraphQL (optional)

- `query invoices(filter: InvoiceFilter): [Invoice]`
- `mutation createInvoice(input: InvoiceInput): Invoice`
- `mutation recordPayment(input: PaymentInput): Payment`

---

## 5. Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API** | FastAPI (Python 3.12) | Modern async framework, automatic OpenAPI docs |
| **Auth** | OAuth2 JWT (PyJWT) | Stateless, compatible with external SSO |
| **ORM** | SQLAlchemy 2.0 | Mature, supports async |
| **DB** | PostgreSQL 16 | ACID, JSONB for event payloads |
| **Cache** | Redis 7 | Session cache, rate limiting |
| **Background Jobs** | RQ (Redis Queue) | Simple, reliable |
| **Messaging** | NATS (optional) | Future event bus |
| **Observability** | Prometheus, Grafana, OpenTelemetry | Metrics, tracing |
| **Containerization** | Docker, Docker‑Compose | Reproducible builds |
| **CI/CD** | GitHub Actions | Lint, tests, integration, image build |
| **Deployment** | Kubernetes (Helm charts) | Autoscaling, secrets management |

---

## 6. Dependencies

| Category | Package | Version |
|----------|---------|---------|
| Core | `fastapi` | ^0.115.0 |
| Core | `uvicorn[standard]` | ^0.30.0 |
| Core | `sqlalchemy` | ^2.0.32 |
| Core | `alembic` | ^1.13.3 |
| Core | `pydantic` | ^2.9.2 |
| Auth | `python-jose` | ^3.3.0 |
| Auth | `passlib[bcrypt]` | ^1.7.4 |
| Cache | `redis` | ^5.0.8 |
| Jobs | `rq` | ^1.15.0 |
| Email | `sendgrid` | ^7.12.0 |
| SMS | `twilio` | ^9.0.0 |
| Testing | `pytest` | ^8.3.2 |
| Lint | `ruff` | ^0.6.7 |
| Docs | `mkdocs-material` | ^9.5.28 |

All dependencies are pinned in `pyproject.toml` and `requirements.txt` for reproducibility.

---

## 7. Deployment

### 7.1 Docker Compose (dev)

```yaml
services:
  api:
    build: .
    command: uvicorn paytracker.api.main:app --host 0.0.0.0 --port 8000 --reload
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - db
      - redis
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: paytracker
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: paytracker
    volumes:
      - pgdata:/var/lib/postgresql/data
  redis:
    image: redis:7
    ports:
      - "6379:6379"
volumes:
  pgdata:
```

### 7.2 Kubernetes (production)

- **Helm Chart**: `charts/paytracker`
- **Secrets**: stored in Vault, injected via CSI driver
- **Horizontal Pod Autoscaler**: based on CPU & request latency
- **Ingress**: NGINX Ingress Controller with TLS termination
- **Monitoring**: Prometheus scrape, Grafana dashboards
- **Backup**: pgBackRest on Rook‑Ceph

### 7.3 CI/CD Pipeline

1. **Lint** (`ruff check .`)
2. **Unit Tests** (`pytest -q`)
3. **Integration Tests** (docker‑compose test env)
4. **Build Docker Image** (`docker build -t paytracker:${{ github.sha }} .`)
5. **Push to Registry** (GitHub Packages / ECR)
6. **Deploy to Staging** (Helm upgrade)
7. **Smoke Tests** (API health, DB connectivity)
8. **Merge to Main** → **Deploy to Prod**

---

## 8. Security & Compliance

- **Password Storage**: Argon2id via `passlib`
- **Transport**: TLS 1.3 enforced
- **Rate Limiting**: Redis‑backed token bucket
- **Audit Logging**: All state changes persisted in `events`
- **GDPR**: Data retention policy (30 days for events, 2 years for invoices)
- **PCI‑DSS**: Payment gateway integration only; no card data stored

---

## 9. Self‑Improving Loop

1. **Event Capture** – Every domain event is stored in `events`.
2. **Feedback API** – Users can rate the usefulness of an event via `/api/v1/feedback`.
3. **Data Pipeline** – A nightly job aggregates events + feedback into the `auto` dataset.
4. **Model Training** – The dataset is fed into the Axentx training pipeline to improve recommendation engines (e.g., next‑payment reminders).

---

## 10. Future Enhancements

| Feature | Priority | Notes |
|---------|----------|-------|
| **GraphQL API** | Medium | For flexible client queries |
| **Webhook Support** | High | Notify external systems on status changes |
| **Multi‑Currency** | Medium | Use `money` library |
| **Advanced Collection Rules** | Low | AI‑driven escalation paths |

---

## 11. Contact & Support

- **Repository**: `arkashira/pay-tracker`
- **Issue Tracker**: GitHub Issues
- **Slack Channel**: `#paytracker-dev`
- **Documentation**: `docs/` folder (MkDocs)

---

*Prepared by: Senior Product/Engineering Lead – Axentx*
