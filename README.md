# 🛠️ pay-tracker

<div align="center">
  <a href="https://github.com/axentx/pay-tracker">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python 3.10">
    <img src="https://img.shields.io/badge/Build-Python%20Poetry-blue.svg" alt="Build: Python Poetry">
    <img src="https://img.shields.io/github/stars/axentx/pay-tracker?style=social" alt="Stars: 0">
  </a>
</div>

---

# 🚀 pay-tracker

**Power finance teams with real-time payment insights.**

A lightweight Python server-side application that aggregates, normalizes, and visualizes real-time payment data from Stripe, PayPal, Square, and CSV feeds.

---

## Why pay-tracker?

* **Real-time payment insights**: Get instant visibility into payment activity across multiple gateways.
* **Multi-gateway support**: Connect to Stripe, PayPal, Square, and custom CSV imports.
* **Role-based access control**: Secure access for analysts, CFOs, auditors, and finance operations teams.
* **Automated reminders**: Trigger emails for overdue payments.
* **Audit-ready reports**: Generate CSV/JSON reports and compliance dashboards.

---

## Feature Overview

| Feature | Description |
| --- | --- |
| Payment Data Aggregation | Collects and normalizes payment data from multiple gateways. |
| Real-time Visualization | Displays payment activity in a user-friendly dashboard. |
| Role-Based Access Control | Secures access for different user roles. |
| Automated Reminders | Triggers emails for overdue payments. |
| Audit-Ready Reports | Generates CSV/JSON reports and compliance dashboards. |

---

## Tech Stack

* Python 3.10

---

## Project Structure

```markdown
business/
docs/
src/
tests/
README.md
pyproject.toml
requirements.txt
```

---

## Getting Started

### Install Dependencies

```bash
poetry install
```

### Run the Application

```bash
poetry run python src/main.py
```

### Run Tests

```bash
poetry run pytest
```

---

## Deploy

### Using Python Poetry

```bash
poetry run python src/main.py
```

---

## Status

Last updated: 2026-06-23T05:45:00.560326Z

Recent commits:

* 5215bee feat(pay-tracker): real, sandbox-tested implementation
* 4faad93 readme-keeper: generate proper project README (overview/stack/run/deploy)
* 7adc1cc feat(pay-tracker): real, sandbox-tested implementation
* 3fa406d readme-keeper: generate proper project README (overview/stack/run/deploy)
* 0a78e8e feat(pay-tracker): real, sandbox-tested implementation
* 40eb608 feat(pay-tracker): real, sandbox-tested implementation
* fc1bcde readme-keeper: generate proper project README (overview/stack/run/deploy)
* 6d4033d feat(pay-tracker): real, sandbox-tested implementation

---

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

MIT License

Copyright (c) 2026 Axentx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.