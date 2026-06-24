<h3 align="center">🛠️ pay-tracker</h3>

<div align="center">
  <a href="https://github.com/axentx/pay-tracker/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/axentx/pay-tracker" alt="License">
  </a>
  <a href="https://github.com/axentx/pay-tracker" target="_blank">
    <img src="https://img.shields.io/github/languages/top/axentx/pay-tracker" alt="Language">
  </a>
  <a href="https://github.com/axentx/pay-tracker/actions" target="_blank">
    <img src="https://img.shields.io/github/workflow/status/axentx/pay-tracker/Build" alt="Build">
  </a>
  <a href="https://github.com/axentx/pay-tracker/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/axentx/pay-tracker" alt="Stars">
  </a>
</div>

---
# 🚀 pay-tracker
**Power finance professionals with streamlined payment tracking and automated collections.** pay-tracker is a lightweight Python server-side application that aggregates, normalizes, and visualizes real-time payment data from Stripe, PayPal, Square, and CSV feeds for finance teams.

## Why pay-tracker?
* **Simplified Payment Tracking**: Easily monitor and filter payment statuses across multiple invoices.
* **Automated Collections**: Streamlined processes for following up on overdue payments, reducing manual effort.
* **Integration Capabilities**: Connects to multiple payment gateways (Stripe, PayPal, Square) via webhooks and polling, as well as custom CSV imports.
* **Role-Based Access Control**: Secure access for analysts, CFOs, auditors, and finance operations teams.
* **Compliance-Ready Reports**: Exposes audit-ready CSV/JSON reports and compliance dashboards.
* **Automated Reminder Emails**: Triggers automated reminder emails for overdue payments.

## Feature Overview
| Feature | Description |
| --- | --- |
| Payment Aggregation | Aggregates payment data from multiple gateways and CSV feeds |
| Data Normalization | Normalizes incoming transaction data for consistent reporting |
| Real-Time Visualization | Visualizes real-time payment data for instant insights |
| Automated Collections | Streamlines processes for following up on overdue payments |
| Role-Based Access Control | Secures access for authorized personnel |
| Compliance-Ready Reports | Exposes audit-ready CSV/JSON reports and compliance dashboards |

## Tech Stack
* Python

## Project Structure
* business: Business logic and domain models
* docs: Documentation and startup artifacts
* src: Core application logic and implementation
* tests: Unit tests and integration tests

## Getting Started
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python -m pay_tracker

# Run tests
python -m unittest discover -s tests
```

## Deploy
```bash
# Deploy to production environment
# NOTE: Deployment commands will be added once the tech stack is locked
```

## Status
pay-tracker is currently in the active stage, with recent commits focused on implementing the core functionality and generating the project README.

## Contributing
Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to pay-tracker.

## License
pay-tracker is licensed under the MIT License. See [LICENSE](LICENSE) for details.