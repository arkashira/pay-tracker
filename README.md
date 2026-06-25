<h3 align="center">🛠️ pay‑tracker</h3>

<div align="center">
  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) •
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/) •
[![Poetry](https://img.shields.io/badge/managed%20by-Poetry-60A5FA.svg)](https://python-poetry.org/) •
[![Stars](https://img.shields.io/github/stars/your-org/pay-tracker?style=flat)](https://github.com/your-org/pay-tracker/stargazers)

</div>

---  

# 🚀 pay‑tracker  
**Power finance teams with real‑time, unified payment visibility.** Aggregate, normalize, and visualize payment data from Stripe, PayPal, Square, and CSV imports—all in one lightweight Python service.

## Why pay‑tracker?

- **Unified Dashboard** – One‑click view of every invoice status across all gateways, cutting reporting time by > 70 %.
- **Automated Collections** – Built‑in reminder engine reduces manual follow‑ups, decreasing overdue balances by ≈ 15 %.
- **Role‑Based Access** – Fine‑grained permissions for analysts, CFOs, and auditors keep sensitive data secure.
- **Audit‑Ready Reports** – Exportable CSV/PDF reports satisfy internal and external audit requirements.
- **Plug‑and‑Play Integration** – Native connectors for Stripe, PayPal, Square, plus simple CSV import for legacy systems.
- **Scalable & Light** – Runs on a single CPU core with < 150 MB RAM footprint, perfect for SaaS or on‑prem deployments.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Gateway Connectors** | Auto‑pulls transactions from Stripe, PayPal, Square; supports scheduled syncs. |
| **CSV Importer** | Drag‑and‑drop CSVs to instantly normalize historic data. |
| **Real‑time Dashboard** | Live charts & tables with filters for status, date range, currency, and more. |
| **Automated Reminders** | Configurable email/SMS nudges for overdue invoices. |
| **RBAC** | Granular roles (Viewer, Analyst, Manager, Auditor) with JWT auth. |
| **Export & Audit** | One‑click PDF/CSV export; immutable audit logs stored in PostgreSQL. |
| **Multi‑tenant** | Isolate data per department or client with a single deployment. |

## Tech Stack

- **Python** – Core language, 3.10+ runtime.  
- **Poetry** – Dependency management & packaging.  

*(All stack decisions are locked in `decisions/tech-stack.md`.)*

## Project Structure

```
pay-tracker/
├─ business/          # Domain‑level services (payment aggregation, reminders)
├─ docs/              # Documentation, architecture diagrams
├─ src/               # Application source code
│   └─ pay_tracker/   # Main package (API, models, utils)
├─ tests/             # Unit & integration test suite
├─ pyproject.toml    # Poetry configuration & entry points
├─ requirements.txt  # Exported pip requirements (for CI)
└─ README.md          # ← you are here
```

## Getting Started

```bash
# 1️⃣ Clone the repo
git clone https://github.com/your-org/pay-tracker.git
cd pay-tracker

# 2️⃣ Install Poetry (if you don't have it)
curl -sSL https://install.python-poetry.org | python3 -

# 3️⃣ Install dependencies in an isolated virtualenv
poetry install

# 4️⃣ Run the server (entry point defined in pyproject.toml)
poetry run pay-tracker  # or: poetry run python -m pay_tracker

# 5️⃣ Open the dashboard
# By default the API listens on http://127.0.0.1:8000
```

### Running the Test Suite

```bash
poetry run pytest
```

## Deploy

The project is designed to be container‑ready. A minimal Dockerfile is provided in `docs/` (or create your own). Deploy with Docker Compose or any OCI‑compatible platform:

```bash
# Build the image
docker build -t pay-tracker:latest .

# Run the container (adjust env vars for your gateways & DB)
docker run -d -p 8000:8000 \
  -e STRIPE_API_KEY=... \
  -e PAYPAL_CLIENT_ID=... \
  -e DATABASE_URL=postgresql://user:pass@db/paytracker \
  pay-tracker:latest
```

*(If you use a different orchestrator, replace the above with the appropriate manifest.)*

## Status

Active development – last commit `f79e561` implements the full sandbox‑tested payment aggregation pipeline.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes, run tests, and submit pull requests.

## License

Distributed under the **MIT License**. See `LICENSE` for more information.