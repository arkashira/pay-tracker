from pay_tracker import PayTracker, Invoice, EmailTemplate
import pytest

def test_add_invoice():
    tracker = PayTracker()
    invoice = Invoice(1, 100.0, '2024-09-20', 0.0, 'pending')
    tracker.add_invoice(invoice)
    assert len(tracker.invoices) == 1

def test_add_email_template():
    tracker = PayTracker()
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    assert len(tracker.email_templates) == 1

def test_send_reminders():
    tracker = PayTracker()
    invoice = Invoice(1, 100.0, '2024-09-15', 0.0, 'pending')
    tracker.add_invoice(invoice)
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    tracker.send_reminders()
    assert len(tracker.sent_emails) == 1

def test_log_sent_emails():
    tracker = PayTracker()
    invoice = Invoice(1, 100.0, '2024-09-15', 0.0, 'pending')
    tracker.add_invoice(invoice)
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    tracker.send_reminders()
    sent_emails = tracker.log_sent_emails()
    assert len(sent_emails) == 1

def test_get_email_template():
    tracker = PayTracker()
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    retrieved_template = tracker.get_email_template(1)
    assert retrieved_template.template == 'Reminder email for invoice {invoice_id}'

def test_update_email_template():
    tracker = PayTracker()
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    tracker.update_email_template(1, 'New reminder email for invoice {invoice_id}')
    retrieved_template = tracker.get_email_template(1)
    assert retrieved_template.template == 'New reminder email for invoice {invoice_id}'

def test_send_reminders_no_template():
    tracker = PayTracker()
    invoice = Invoice(1, 100.0, '2024-09-15', 0.0, 'pending')
    tracker.add_invoice(invoice)
    tracker.send_reminders()
    assert len(tracker.sent_emails) == 0

def test_send_reminders_no_invoices():
    tracker = PayTracker()
    template = EmailTemplate(1, 'Reminder email for invoice {invoice_id}')
    tracker.add_email_template(template)
    tracker.send_reminders()
    assert len(tracker.sent_emails) == 0
