```markdown
# Dataflow Architecture for Pay-Tracker

## External Data Sources
- **Payment Gateways**: APIs from Stripe, PayPal, Square, etc. for payment status updates.
- **Accounting Software**: Integrations with QuickBooks, Xero, etc. for invoice data.
- **Bank APIs**: For direct bank transaction status and reconciliation.
- **User Input**: Manual entry of payment statuses and notes by users.

## Ingestion Layer
- **API Gateway**: Handles incoming requests from external sources and user interfaces.
- **Webhook Listener**: Listens for real-time updates from payment gateways and accounting software.
- **Batch Processor**: Scheduled jobs to pull data from accounting software and bank APIs.

## Processing/Transform Layer
- **Data Normalization Service**: Standardizes incoming data formats from various sources.
- **Business Logic Engine**: Applies rules for payment status tracking, filtering, and collections.
- **Notification Service**: Sends alerts and updates to users based on payment status changes.

## Storage Tier
- **Relational Database**: Stores structured data for invoices, payment statuses, and user accounts.
- **NoSQL Database**: Stores unstructured data such as logs, notifications, and user interactions.
- **Cache Layer**: In-memory caching for frequently accessed data to improve performance.

## Query/Serving Layer
- **GraphQL API**: Provides a flexible interface for clients to query payment data and statuses.
- **REST API**: Legacy support for existing integrations and clients.
- **Analytics Dashboard**: Real-time insights and reporting for users on payment statuses and trends.

## Egress to User
- **Web Application**: User interface for developers and businesses to track payments and manage invoices.
- **Mobile Application**: Lightweight app for on-the-go access to payment statuses.
- **Email Notifications**: Regular updates and alerts sent to users regarding payment statuses.

```

### ASCII Block Diagram

```
+-------------------+       +-------------------+       +-------------------+
|  External Data    |       |   Ingestion Layer  |       | Processing/Transform|
|     Sources       |       |                   |       |        Layer        |
|                   |       |                   |       |                     |
|  Payment Gateways | ----> |   API Gateway     | ----> | Data Normalization  |
|  Accounting Soft. | ----> |   Webhook Listener | ----> | Business Logic Engine|
|  Bank APIs        | ----> |   Batch Processor  | ----> | Notification Service |
|  User Input       |       |                   |       |                     |
+-------------------+       +-------------------+       +-------------------+
                                                               |
                                                               v
+-------------------+       +-------------------+       +-------------------+
|   Storage Tier    |       | Query/Serving Layer|       | Egress to User    |
|                   |       |                   |       |                   |
| Relational DB     | <---- |   GraphQL API     | <---- | Web Application    |
| NoSQL DB          |       |   REST API        |       | Mobile Application |
| Cache Layer       |       |   Analytics Dash.  |       | Email Notifications |
+-------------------+       +-------------------+       +-------------------+
```