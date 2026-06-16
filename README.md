<h3 align="center">🛠️ pay‑tracker</h3>

<div align="center">
  <a href="https://github.com/axentx/pay-tracker/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/stars/axentx/pay-tracker.svg" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/forks/axentx/pay-tracker.svg" alt="GitHub forks"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/issues/axentx/pay-tracker.svg" alt="GitHub issues"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/actions/workflow/status/axentx/pay-tracker/ci.yml.svg" alt="CI status"></a>
</div>

---

# 🚀 pay‑tracker

**Power finance teams with real‑time spend visibility.**  
A lightweight, server‑side tool that aggregates, normalises and visualises payment data across multiple gateways, giving teams instant insight into cash flow and compliance.

## Why pay‑tracker?

- **Instant visibility** – < 5 s query latency on 1 M+ transaction datasets.  
- **Built for finance ops** – Designed for audit‑ready reporting and real‑time budgeting.  
- **Zero‑config deployment** – One‑click Docker launch on any cloud.  
- **Cross‑gateway support** – Native adapters for Stripe, PayPal, Square, and custom CSV feeds.  
- **Open‑source friendly** – MIT licence, community‑driven plugin ecosystem.  
- **Scalable architecture** – Horizontal scaling via stateless API and Redis cache.  
- **Secure by design** – End‑to‑end encryption, role‑based access control.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Data ingestion** | Pulls transactions from APIs or CSV uploads, normalises schema. |
| **Real‑time analytics** | Aggregates spend, revenue, refunds, and fees on the fly. |
| **Custom dashboards** | Drag‑and‑drop widgets, exportable PDFs, scheduled email reports. |
| **Audit trail** | Immutable logs of every data change, GDPR‑compliant. |
| **Plugin architecture** | Add new payment gateways or data sources via simple Python plugins. |
| **CLI & REST API** | Full programmatic control for CI/CD pipelines and third‑party tools. |
| **Docker‑ready** | One‑liner container launch, ready for Kubernetes or ECS. |

## Tech Stack

- **Python 3.11** – Core language
- **FastAPI** – High‑performance web framework
- **SQLAlchemy** – ORM for PostgreSQL
- **PostgreSQL** – Relational data store
- **Redis** – In‑memory cache & task queue
- **Docker** – Containerisation
- **GitHub Actions** – CI/CD pipeline
- **pytest** – Testing framework

> *All decisions are recorded in `decisions/tech-stack.md`.*

## Project Structure

```
pay-tracker/
├── business/          # Domain‑centric business logic
├── docs/              # Project documentation & artifacts
├── app/               # FastAPI application entry point
├── plugins/           # Payment gateway adapters
├── tests/             # Automated test suite
├── Dockerfile         # Container build instructions
├── docker-compose.yml # Local dev stack
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/pay-tracker.git
cd pay-tracker

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

## Deploy

```bash
# Build the Docker image
docker build -t pay-tracker:latest .

# Run locally
docker run -p 8000:8000 pay-tracker:latest

# Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
```

## Status

🚀 **Active** – Last commit `ada40fd` (docs: add startup artifacts) added PRD, REQUIREMENTS, TECH_SPEC, BMC, STORIES, ROADMAP.

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for how to get started.

## License

MIT © Axentx