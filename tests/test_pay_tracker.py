from pay_tracker import PayTracker, Invoice, parse_date
import pytest
from datetime import datetime, timedelta
import json

@pytest.fixture
def pay_tracker():
    return PayTracker()

def test_add_invoice(pay_tracker):
    invoice = Invoice(1, 100.0, '2024-09-16', 'unpaid')
    pay_tracker.add_invoice(invoice)
    assert len(pay_tracker.invoices) == 1

def test_prioritize_invoices(pay_tracker):
    invoice1 = Invoice(1, 100.0, '2024-09-16', 'unpaid')
    invoice2 = Invoice(2, 50.0, '2024-09-15', 'unpaid')
    pay_tracker.add_invoice(invoice1)
    pay_tracker.add_invoice(invoice2)
    prioritized_invoices = pay_tracker.prioritize_invoices()
    assert prioritized_invoices[0].id == 1

def test_save_prioritized_list(pay_tracker, tmp_path):
    invoice1 = Invoice(1, 100.0, '2024-09-16', 'unpaid')
    invoice2 = Invoice(2, 50.0, '2024-09-15', 'unpaid')
    pay_tracker.add_invoice(invoice1)
    pay_tracker.add_invoice(invoice2)
    filename = tmp_path / 'prioritized_list.json'
    pay_tracker.save_prioritized_list(filename)
    with open(filename, 'r') as f:
        loaded_list = json.load(f)
    assert len(loaded_list) == 2

def test_load_prioritized_list(pay_tracker, tmp_path):
    filename = tmp_path / 'prioritized_list.json'
    with open(filename, 'w') as f:
        json.dump([{'id': 1, 'amount': 100.0, 'due_date': '2024-09-16'}], f)
    loaded_list = pay_tracker.load_prioritized_list(filename)
    assert len(loaded_list) == 1

def test_send_notifications(pay_tracker):
    invoice = Invoice(1, 100.0, '2024-09-01', 'unpaid')
    pay_tracker.add_invoice(invoice)
    pay_tracker.send_notifications()

def test_parse_date_valid():
    date_str = '2024-09-16'
    result = parse_date(date_str)
    assert result == datetime(2024, 9, 16)

def test_parse_date_invalid():
    date_str = 'invalid_date'
    with pytest.raises(ValueError):
        parse_date(date_str)
