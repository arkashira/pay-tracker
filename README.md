<h3 align="center">🛠️ pay‑tracker</h3>

<div align="center">
  <a href="https://github.com/axentx/pay-tracker/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/pay-tracker.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/stars/axentx/pay-tracker.svg?style=flat-square" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/pay-tracker/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/pay-tracker/ci.yml?style=flat-square" alt="Build"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/languages/top/axentx/pay-tracker.svg?style=flat-square" alt="Language"></a>
</div>

---

# 🚀 pay‑tracker

**Power finance teams with real‑time payment visibility.**  
A lightweight, server‑side tool that aggregates, normalizes, and visualizes payment data from Stripe, PayPal, Square, and custom CSV feeds, delivering audit‑ready reporting and compliance dashboards.

## Why pay‑tracker?

- **Instant Spend Visibility** – 100 % of transactions are pulled and displayed within 30 seconds of ingestion.  
- **Built for Finance Teams** – Designed for analysts and CFOs who need real‑time budgeting and audit trails.  
- **Automated Collections** – Auto‑flag overdue payments and trigger follow‑up workflows.  
- **Multi‑Gateway Support** – Native connectors for Stripe, PayPal, Square, plus CSV import.  
- **Compliance‑Ready** – Generates audit‑ready reports in PDF/CSV format on demand.  
- **Scalable Architecture** – Stateless API with Redis caching; Docker‑ready for horizontal scaling.  
- **Role‑Based Access Control** – Fine‑grained permissions for sensitive financial data.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Gateway Aggregation** | Pulls transactions from Stripe, PayPal, Square, and CSV feeds. |
| **Schema Normalization** | Converts disparate payloads into a unified internal model. |
| **Real‑Time Analytics** | Live dashboards for spend, aging, and revenue forecasting. |
| **Audit‑Ready Reporting** | Export PDF/CSV reports with full audit trail metadata. |
| **Automated Collections** | Auto‑detect overdue invoices and trigger email reminders. |
| **Role‑Based Access** | Granular permissions for read/write/analytics. |
| **Docker‑Ready** | `docker-compose` for local dev and production deployment. |

## Tech Stack

- Docker  
- Redis  
- API (FastAPI)  
- Stripe  
- PayPal  
- Square  

## Project Structure

```
pay‑tracker/
├── business/          # Business logic and domain models
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # Core application code
│   ├── api/           # FastAPI endpoints
│   ├── gateways/      # Stripe/PayPal/Square connectors
│   ├── models/        # Normalized data schemas
│   └── services/      # Aggregation, reporting, and caching
├── tests/             # Unit and integration tests
├── Dockerfile         # Build image
├── docker-compose.yml # Local dev stack
├── pyproject.toml     # Project metadata & dependencies
└── requirements.txt   # Runtime requirements
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/pay-tracker.git
cd pay-tracker

# Build the Docker image
docker build -t pay-tracker .

# Start the services (API + Redis)
docker compose up -d

# Verify API is running
curl http://localhost:8000/docs
```

## Deploy

```bash
# Production deployment with Docker Compose
docker compose -f docker-compose.prod.yml up -d
```

> **Tip:** Set environment variables for Stripe, PayPal, and Square API keys in `.env` before starting the stack.

## Status

Active – last commit `6d4033d` (2026‑06‑19): real, sandbox‑tested implementation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Axentx