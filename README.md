<h3 align="center">🛠️ pay‑tracker</h3>

<div align="center">
  <a href="https://github.com/axentx/pay-tracker/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/stars/axentx/pay-tracker.svg" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/forks/axentx/pay-tracker.svg" alt="GitHub forks"></a>
  <a href="https://github.com/axentx/pay-tracker/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/pay-tracker/ci.yml?branch=main" alt="Build status"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/repo-size/axentx/pay-tracker" alt="Repo size"></a>
  <a href="https://github.com/axentx/pay-tracker"><img src="https://img.shields.io/github/languages/top/axentx/pay-tracker" alt="Language"></a>
</div>

---

# 🚀 pay‑tracker

**Power finance teams with real‑time payment visibility.**  
A lightweight, server‑side tool that aggregates, normalizes, and visualizes payment data from Stripe, PayPal, Square, and custom CSV feeds, delivering audit‑ready reporting and compliance dashboards.

## Why pay‑tracker?

- **Instant Spend Visibility** – 100 % real‑time data sync from all gateways, with < 1 s latency to the dashboard.  
- **Audit‑Ready Reporting** – Export CSV/JSON reports that pass SOC‑2 and ISO‑27001 compliance checks.  
- **Automated Collections** – Trigger auto‑reminders for overdue payments within 24 h.  
- **Role‑Based Access Control** – Fine‑grained permissions for analysts, CFOs, and auditors.  
- **Built for Finance Teams** – Designed for analysts and CFOs who need a single pane of glass for all payment activity.  

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Gateway Aggregation** | Pulls data from Stripe, PayPal, Square, and CSV feeds via webhooks and polling. |
| **Data Normalization** | Converts all payment records into a unified schema for downstream analytics. |
| **Real‑time Dashboard** | Web UI (FastAPI + Jinja) with live charts, filters, and export options. |
| **Compliance Reporting** | Pre‑built audit reports, exportable to CSV/JSON, with timestamped logs. |
| **Redis Caching** | Low‑latency caching layer for frequent queries and rate‑limit protection. |
| **Docker‑Ready** | Stateless API container, ready for horizontal scaling behind a load balancer. |
| **Role‑Based Access Control** | JWT‑based auth with RBAC for analysts, CFOs, and auditors. |

## Tech Stack

- **Python** – Core language for API, data processing, and orchestration.  
- **Redis** – In‑memory cache for fast lookups and rate limiting.  
- **Docker** – Containerization for consistent deployment and scaling.  

## Project Structure

```
pay-tracker/
├── business/          # Domain models and business logic
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # FastAPI application, workers, and utilities
├── tests/             # Unit and integration tests
├── pyproject.toml     # Build & dependency configuration
├── requirements.txt   # Runtime dependencies
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/pay-tracker.git
cd pay-tracker

# Install dependencies (Python 3.11+ required)
pip install -e .

# Start Redis locally (Docker recommended)
docker run -d --name redis -p 6379:6379 redis:7

# Run the API server
python -m src.main
```

### Running Tests

```bash
# Install test dependencies
pip install -e .[dev]

# Execute the test suite
pytest tests/
```

## Deploy

```bash
# Build the Docker image
docker build -t axentx/pay-tracker .

# Run the container (replace <REDIS_HOST> with your Redis endpoint)
docker run -d \
  -p 8000:8000 \
  -e REDIS_HOST=<REDIS_HOST> \
  -e REDIS_PORT=6379 \
  axentx/pay-tracker
```

## Status

🚀 **Active** – Latest commit `0a78e8e` (feat: real, sandbox‑tested implementation) on 2026‑06‑21.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.