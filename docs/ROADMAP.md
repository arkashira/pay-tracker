# Roadmap – pay‑tracker

## Vision

Build a lightweight, developer‑friendly billing & invoicing system that lets teams:

* Create, edit and archive invoices in a single place  
* Track payment status in real time  
* Filter and sort by status, due date, customer, or amount  
* Automate collection workflows (reminders, escalations, and dispute handling)  

The product will be shipped as a self‑hosted SaaS (Docker + Helm) and a lightweight CLI for quick prototyping.

---

## Release Cadence

| Release | Target Date | Focus |
|---------|-------------|-------|
| **MVP** | **2026‑07‑30** | Core invoice CRUD + status tracking + basic reporting |
| **v1.0** | 2026‑10‑15 | Advanced filtering, recurring invoices, basic reminders |
| **v1.1** | 2026‑12‑01 | Integration with Stripe/PayPal, webhook support |
| **v2.0** | 2027‑03‑15 | Full collection workflow, analytics dashboard, API v2 |

---

## MVP Milestone (Must‑Have for Launch)

| Feature | Owner | Acceptance Criteria | Notes |
|---------|-------|---------------------|-------|
| **Invoice CRUD** | Backend | REST endpoints: `POST /invoices`, `GET /invoices/:id`, `PUT /invoices/:id`, `DELETE /invoices/:id` | Use PostgreSQL + Prisma. |
| **Payment Status** | Backend | Status enum (`draft`, `sent`, `paid`, `overdue`, `disputed`) stored in DB | Status transitions validated by business rules. |
| **Filtering & Sorting** | Frontend | UI table supports filter by status, date range, amount, customer; sort by any column | Use React + TanStack Table. |
| **Dashboard** | Frontend | Summary cards: Total Invoices, Total Outstanding, Overdue Count | Simple chart with Recharts. |
| **Docker + Helm** | Ops | Production‑ready Docker image; Helm chart for K8s | Use `arkashira/surrogate-1-harvest` as base. |
| **Unit & Integration Tests** | QA | ≥80 % coverage on core logic | Use Jest + Supertest. |
| **CI/CD** | DevOps | GitHub Actions: lint, test, build, push image | Leverage existing `arkashira` workflow. |
| **Documentation** | Technical Writer | README, API spec (OpenAPI), deployment guide | Auto‑generate from OpenAPI. |

> **MVP‑Critical**: Invoice CRUD, Payment Status, Filtering, Docker/Helm, CI/CD, Docs.

---

## v1.0 – Core Enhancements

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **Recurring Invoices** | Create recurring templates | Backend | Endpoint to create/update recurring invoice; scheduler to auto‑generate invoices |
| **Reminder System** | Email/SMS reminders for overdue invoices | Backend | Configurable reminder schedule; integration with SendGrid |
| **Bulk Operations** | Bulk edit/delete invoices | Frontend | Multi‑select table with bulk actions |
| **Export** | CSV/Excel export of invoice list | Backend | `/invoices/export` endpoint |
| **User Roles** | Admin / Accountant / Viewer | Backend | RBAC with JWT; UI role‑based access |

---

## v1.1 – Payment Processor Integration

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **Stripe Integration** | Create payment intent, capture | Backend | Webhook handling, status sync |
| **PayPal Integration** | Checkout flow | Backend | OAuth flow, IPN handling |
| **Unified Webhook** | Single endpoint for all processors | Backend | Idempotent processing, retry logic |
| **Payment History** | View past payments per invoice | Frontend | Table with pagination |

---

## v2.0 – Collection & Analytics

| Theme | Feature | Owner | Acceptance Criteria |
|-------|---------|-------|---------------------|
| **Collection Workflow** | Escalation tiers, dispute resolution | Backend | State machine for collection stages |
| **Analytics Dashboard** | KPI cards, trend charts | Frontend | Real‑time data via GraphQL |
| **API v2** | Versioned GraphQL API | Backend | Deprecate REST, support migrations |
| **Mobile‑Friendly UI** | Responsive design | Frontend | Works on iOS/Android browsers |
| **Audit Trail** | Immutable logs of changes | Backend | Append‑only log table, exportable |

---

## Technical Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API** | Node.js + Express + Prisma | Fast, type‑safe, fits existing repo |
| **DB** | PostgreSQL | ACID, supports JSONB for flexible fields |
| **Auth** | JWT + OAuth2 | Stateless, easy to integrate with external IdPs |
| **Frontend** | React + Vite + TanStack Table | Modern, lightweight, supports server‑side rendering |
| **Testing** | Jest + Supertest + Cypress | Full stack coverage |
| **CI/CD** | GitHub Actions | Existing pipelines in `arkashira` repo |
| **Containerization** | Docker + Helm | Consistent deployment across environments |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Payment Processor downtime** | High | Implement retry/back‑off, fallback to manual capture |
| **Data consistency** | Medium | Use transactions, optimistic locking |
| **Regulatory compliance (PCI‑DSS)** | High | Off‑load card data to processors, store only tokens |
| **User adoption** | Medium | Provide quick‑start templates, in‑app tutorials |

---

## Success Metrics

| Metric | Target | Tool |
|--------|--------|------|
| **Time to first invoice** | < 5 min | User onboarding analytics |
| **Invoice creation rate** | 80 % of users create > 10 invoices | Mixpanel |
| **Payment capture rate** | 90 % of sent invoices paid within 30 days | Stripe/PayPal dashboards |
| **Churn** | < 5 % monthly | Cohort analysis |

---

## Dependencies

* **Stripe** and **PayPal** SDKs (open‑source)
* **SendGrid** for email reminders
* **PostgreSQL** (self‑hosted or managed)
* **Redis** for caching and job queue (BullMQ)

---

## Timeline (Gantt‑style)

```
2026-07-01 |---MVP---| 2026-07-30
2026-08-01 |---v1.0---| 2026-10-15
2026-10-16 |---v1.1---| 2026-12-01
2026-12-02 |---v2.0---| 2027-03-15
```

---

### Next Steps

1. Finalize MVP backlog and assign tickets.  
2. Set up CI/CD for automated linting, testing, and image publishing.  
3. Kick‑off sprint 0: environment provisioning, database schema design.  

---
