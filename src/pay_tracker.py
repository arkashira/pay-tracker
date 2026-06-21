import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Invoice:
    id: int
    amount: float
    due_date: str
    paid_amount: float
    status: str

@dataclass
class EmailTemplate:
    id: int
    template: str

class PayTracker:
    def __init__(self):
        self.invoices = []
        self.email_templates = []
        self.sent_emails = []

    def add_invoice(self, invoice: Invoice):
        self.invoices.append(invoice)

    def add_email_template(self, template: EmailTemplate):
        self.email_templates.append(template)

    def send_reminders(self):
        for invoice in self.invoices:
            due_date = datetime.strptime(invoice.due_date, '%Y-%m-%d')
            today = datetime.today()
            if today > due_date or invoice.paid_amount < invoice.amount:
                template = next((t for t in self.email_templates if t.id == 1), None)
                if template:
                    email_body = template.template.replace('{invoice_id}', str(invoice.id))
                    self.sent_emails.append(email_body)

    def log_sent_emails(self):
        return self.sent_emails

    def get_email_template(self, id: int):
        return next((t for t in self.email_templates if t.id == id), None)

    def update_email_template(self, id: int, new_template: str):
        template = self.get_email_template(id)
        if template:
            template.template = new_template
