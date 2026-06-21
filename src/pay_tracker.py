import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Invoice:
    id: int
    due_date: str
    status: str
    amount: float
    paid: float

@dataclass
class EmailTemplate:
    subject: str
    body: str

class PayTracker:
    def __init__(self):
        self.invoices = []
        self.email_templates = {}
        self.sent_emails = []

    def add_invoice(self, invoice: Invoice):
        self.invoices.append(invoice)

    def add_email_template(self, template_id: str, template: EmailTemplate):
        self.email_templates[template_id] = template

    def send_reminders(self):
        for invoice in self.invoices:
            if invoice.status == 'partial' or invoice.due_date < datetime.now().strftime('%Y-%m-%d'):
                template = self.email_templates.get('reminder')
                if template:
                    email = {
                        'subject': template.subject,
                        'body': template.body,
                        'invoice_id': invoice.id
                    }
                    self.sent_emails.append(email)

    def log_email(self, email):
        self.sent_emails.append(email)

    def get_sent_emails(self, invoice_id: int):
        return [email for email in self.sent_emails if email['invoice_id'] == invoice_id]

    def edit_email_template(self, template_id: str, new_template: EmailTemplate):
        if template_id in self.email_templates:
            self.email_templates[template_id] = new_template
        else:
            raise ValueError('Template not found')

    def get_email_template(self, template_id: str):
        return self.email_templates.get(template_id)
