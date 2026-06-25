from dataclasses import dataclass
from enum import Enum
from typing import List

class InvoiceStatus(str, Enum):
    ALL = "all"
    UNPAID = "unpaid"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"

@dataclass
class Invoice:
    id: int
    status: str
    amount: float
    paid_amount: float

class PayTracker:
    def __init__(self, invoices: List[Invoice]):
        self.invoices = invoices

    def filter_invoices(self, status: InvoiceStatus) -> List[Invoice]:
        if status == InvoiceStatus.ALL:
            return self.invoices
        elif status == InvoiceStatus.UNPAID:
            return [invoice for invoice in self.invoices if invoice.paid_amount == 0]
        elif status == InvoiceStatus.PARTIALLY_PAID:
            return [invoice for invoice in self.invoices if 0 < invoice.paid_amount < invoice.amount]
        elif status == InvoiceStatus.PAID:
            return [invoice for invoice in self.invoices if invoice.paid_amount == invoice.amount]

    def get_invoices_count(self, status: InvoiceStatus) -> int:
        return len(self.filter_invoices(status))
