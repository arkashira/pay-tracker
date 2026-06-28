```markdown
# Tech Spec for Pay-Tracker

## Stack
- **Language**: Python
- **Framework**: FastAPI
- **Runtime**: Python 3.9+

## Hosting
- **Platform**: 
  - Heroku (Free-tier for initial deployment)
  - AWS (for scaling post-validation)
  - DigitalOcean (for cost-effective hosting with managed databases)

## Data Model
### Tables/Collections
1. **Users**
   - `user_id` (UUID, Primary Key)
   - `email` (String, Unique)
   - `password_hash` (String)
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)

2. **Invoices**
   - `invoice_id` (UUID, Primary Key)
   - `user_id` (UUID, Foreign Key)
   - `amount` (Decimal)
   - `status` (Enum: 'pending', 'paid', 'failed', 'partially_paid')
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)

3. **Payments**
   - `payment_id` (UUID, Primary Key)
   - `invoice_id` (UUID, Foreign Key)
   - `amount` (Decimal)
   - `payment_date` (Timestamp)
   - `status` (Enum: 'completed', 'failed', 'pending')

4. **Payment_Status**
   - `status_id` (UUID, Primary Key)
   - `invoice_id` (UUID, Foreign Key)
   - `status` (String)
   - `timestamp` (Timestamp)

## API Surface
1. **User Registration**
   - **Method**: POST
   - **Path**: `/api/users/register`
   - **Purpose**: Register a new user.

2. **User Login**
   - **Method**: POST
   - **Path**: `/api/users/login`
   - **Purpose**: Authenticate user and return a token.

3. **Create Invoice**
   - **Method**: POST
   - **Path**: `/api/invoices`
   - **Purpose**: Create a new invoice for the authenticated user.

4. **Get Invoice Status**
   - **Method**: GET
   - **Path**: `/api/invoices/{invoice_id}`
   - **Purpose**: Retrieve the status and details of a specific invoice.

5. **Record Payment**
   - **Method**: POST
   - **Path**: `/api/payments`
   - **Purpose**: Record a payment against an invoice.

6. **Get All Invoices**
   - **Method**: GET
   - **Path**: `/api/invoices`
   - **Purpose**: Retrieve all invoices for the authenticated user.

7. **Update Invoice Status**
   - **Method**: PATCH
   - **Path**: `/api/invoices/{invoice_id}/status`
   - **Purpose**: Update the status of an invoice.

8. **Get Payment History**
   - **Method**: GET
   - **Path**: `/api/payments`
   - **Purpose**: Retrieve payment history for the authenticated user.

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for user sessions.
- **Secrets Management**: Use AWS Secrets Manager or HashiCorp Vault for sensitive data (e.g., database credentials).
- **IAM**: Role-based access control (RBAC) for API endpoints, ensuring users can only access their own data.

## Observability
- **Logs**: Use structured logging with Loguru for Python.
- **Metrics**: Integrate Prometheus for monitoring key performance indicators (KPIs) such as request counts, error rates, and response times.
- **Traces**: Use OpenTelemetry for distributed tracing to monitor API performance and identify bottlenecks.

## Build/CI
- **Version Control**: GitHub for source code management.
- **CI/CD**: GitHub Actions for continuous integration and deployment.
  - **Build**: Run tests on every pull request.
  - **Deploy**: Automatic deployment to Heroku on merging to the main branch.
```
