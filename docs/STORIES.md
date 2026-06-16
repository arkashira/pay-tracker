# STORIES.md

## Product: pay‑tracker  
*A billing and invoicing management system that simplifies payment status tracking, filtering, and collections for developers and businesses.*

---

## Epic 1 – Core Invoice Lifecycle  
**Goal**: Enable users to create, view, and manage invoices from a single interface.

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 1.1 | **As a developer, I want to create a new invoice, so that I can bill clients quickly.** | • Invoice form includes fields: `client`, `description`, `amount`, `due_date`, `status` (draft, sent, paid, overdue). <br>• Validation errors are shown inline. <br>• On submit, invoice is persisted and a `draft` status is assigned. |
| 1.2 | **As a developer, I want to view a list of my invoices, so that I can see all outstanding work at a glance.** | • Paginated table shows `invoice_id`, `client`, `amount`, `due_date`, `status`. <br>• Table supports sorting by any column. <br>• Clicking an invoice opens a detail view. |
| 1.3 | **As a developer, I want to edit an existing invoice, so that I can correct mistakes before sending.** | • Edit form pre‑populated with current values. <br>• Only invoices with status `draft` or `sent` can be edited. <br>• Changes are persisted on save. |
| 1.4 | **As a developer, I want to delete a draft invoice, so that I can remove unnecessary entries.** | • Confirmation dialog appears. <br>• Only invoices with status `draft` can be deleted. <br>• Deleted invoice is removed from the list. |
| 1.5 | **As a developer, I want to change an invoice status to `sent`, so that I can notify the client.** | • Status transition button appears on invoice detail. <br>• Transition triggers an email notification (mocked in dev). <br>• Status is updated in the database. |

---

## Epic 2 – Payment Tracking & Status Updates  
**Goal**: Provide real‑time visibility into payment progress and automate status changes.

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 2.1 | **As a developer, I want to mark an invoice as `paid`, so that my records reflect the latest state.** | • Status button available only for `sent` invoices. <br>• On click, status changes to `paid` and a timestamp is recorded. |
| 2.2 | **As a developer, I want the system to automatically flag overdue invoices, so that I can prioritize collections.** | • Background job runs nightly. <br>• Invoices past `due_date` and not `paid` are marked `overdue`. <br>• Overdue invoices are highlighted in the UI. |
| 2.3 | **As a developer, I want to view a payment history for each invoice, so that I can audit past transactions.** | • Payment history panel shows `payment_id`, `amount`, `date`, `method`. <br>• Ability to add a manual payment record. |
| 2.4 | **As a developer, I want to set up automatic reminders for overdue invoices, so that I reduce manual follow‑ups.** | • Configurable reminder frequency (e.g., 3, 7, 14 days). <br>• Reminder emails are queued and sent via background worker. |

---

## Epic 3 – Filtering & Reporting  
**Goal**: Empower users to slice and dice invoice data for insights and compliance.

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 3.1 | **As a developer, I want to filter invoices by status, client, and date range, so that I can focus on specific subsets.** | • Filter UI supports multi‑select status, text search for client, and date pickers for `created_at` and `due_date`. <br>• Filters update the list in real time. |
| 3.2 | **As a developer, I want to export filtered invoices to CSV, so that I can share data with stakeholders.** | • Export button triggers CSV download containing current filter results. <br>• CSV includes all visible columns. |
| 3.3 | **As a developer, I want to view a dashboard of key metrics (total invoices, paid %, overdue %, revenue), so that I can monitor business health.** | • Dashboard displays KPI cards with real‑time data. <br>• Metrics are calculated from the database. |
| 3.4 | **As a developer, I want to schedule automated PDF invoices, so that clients receive professional documents.** | • PDF generation uses a template engine. <br>• PDFs are emailed to the client on status `sent`. |

---

## Epic 4 – Security & Permissions  
**Goal**: Ensure data integrity and appropriate access control.

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 4.1 | **As an admin, I want to assign roles (admin, developer, accountant) to users, so that I can control access.** | • Role assignment UI in user settings. <br>• Roles stored in the database. |
| 4.2 | **As a user, I want to see only invoices belonging to my organization, so that data is isolated.** | • Multi‑tenant architecture: all queries filter by `org_id`. <br>• No cross‑org data leakage. |
| 4.3 | **As a developer, I want to audit logs for invoice changes, so that I can trace modifications.** | • Every create/edit/delete/status change logs `user_id`, `action`, `timestamp`. <br>• Logs are viewable in an audit panel. |

---

## Epic 5 – Integration & Extensibility  
**Goal**: Allow pay‑tracker to connect with external services and be extended by partners.

| # | User Story | Acceptance Criteria |
|---|-------------|---------------------|
| 5.1 | **As a developer, I want to integrate with Stripe for payment capture, so that I can automate payment status updates.** | • Stripe webhook endpoint receives `payment_intent.succeeded`. <br>• Invoice status is updated to `paid` automatically. |
| 5.2 | **As a developer, I want to expose a REST API for invoice CRUD, so that external tools can consume data.** | • Endpoints: `GET /invoices`, `POST /invoices`, `PUT /invoices/:id`, `DELETE /invoices/:id`. <br>• API uses token‑based auth. |
| 5.3 | **As a developer, I want to add custom fields to invoices, so that I can capture domain‑specific data.** | • Admin UI allows adding field definitions. <br>• Custom fields appear in forms and reports. |

---

## MVP Release Order

1. **Epic 1** – Core Invoice Lifecycle  
2. **Epic 2** – Payment Tracking & Status Updates  
3. **Epic 3** – Filtering & Reporting  
4. **Epic 4** – Security & Permissions  
5. **Epic 5** – Integration & Extensibility  

---

### Notes for Implementation

- **Tech Stack**: Rails 7 backend, PostgreSQL, React front‑end, Sidekiq for background jobs, ActionMailer for emails, Stripe SDK for payments.  
- **Testing**: RSpec for unit & integration tests, Cypress for end‑to‑end.  
- **CI/CD**: GitHub Actions pipeline with linting, tests, and Docker image build.  
- **Documentation**: Swagger UI for API docs, Markdown docs for internal use.  

---
