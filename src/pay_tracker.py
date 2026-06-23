import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Invoice:
    id: int
    amount: float
    due_date: str
    payment_status: str

class PayTracker:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def prioritize_invoices(self):
        return sorted(self.invoices, key=lambda x: (x.due_date, x.amount), reverse=True)

    def save_prioritized_list(self, filename):
        with open(filename, 'w') as f:
            json.dump([{'id': i.id, 'amount': i.amount, 'due_date': i.due_date} for i in self.prioritize_invoices()], f)

    def load_prioritized_list(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def send_notifications(self):
        overdue_invoices = [i for i in self.invoices if datetime.strptime(i.due_date, '%Y-%m-%d') < datetime.now()]
        for invoice in overdue_invoices:
            print(f"Notification: Invoice {invoice.id} is overdue")

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format")
