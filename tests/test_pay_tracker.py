from pay_tracker import PayTracker, Invoice, EmailTemplate
import pytest

@pytest.fixture
def pay_tracker():
    return PayTracker()

def test_add_invoice(pay_tracker):
    invoice = Invoice(1, '2024-09-16', 'partial', 100.0, 50.0)
    pay_tracker.add_invoice(invoice)
    assert len(pay_tracker.invoices) == 1

def test_add_email_template(pay_tracker):
    template = EmailTemplate('Reminder', 'Please pay your invoice')
    pay_tracker.add_email_template('reminder', template)
    assert pay_tracker.get_email_template('reminder') == template

def test_send_reminders(pay_tracker):
    invoice = Invoice(1, '2024-09-16', 'partial', 100.0, 50.0)
    pay_tracker.add_invoice(invoice)
    template = EmailTemplate('Reminder', 'Please pay your invoice')
    pay_tracker.add_email_template('reminder', template)
    pay_tracker.send_reminders()
    assert len(pay_tracker.sent_emails) == 1

def test_log_email(pay_tracker):
    email = {'subject': 'Reminder', 'body': 'Please pay your invoice', 'invoice_id': 1}
    pay_tracker.log_email(email)
    assert len(pay_tracker.sent_emails) == 1

def test_get_sent_emails(pay_tracker):
    email1 = {'subject': 'Reminder', 'body': 'Please pay your invoice', 'invoice_id': 1}
    email2 = {'subject': 'Reminder', 'body': 'Please pay your invoice', 'invoice_id': 2}
    pay_tracker.log_email(email1)
    pay_tracker.log_email(email2)
    assert len(pay_tracker.get_sent_emails(1)) == 1

def test_edit_email_template(pay_tracker):
    template = EmailTemplate('Reminder', 'Please pay your invoice')
    pay_tracker.add_email_template('reminder', template)
    new_template = EmailTemplate('New Reminder', 'Please pay your new invoice')
    pay_tracker.edit_email_template('reminder', new_template)
    assert pay_tracker.get_email_template('reminder') == new_template

def test_get_email_template(pay_tracker):
    template = EmailTemplate('Reminder', 'Please pay your invoice')
    pay_tracker.add_email_template('reminder', template)
    assert pay_tracker.get_email_template('reminder') == template

def test_edit_email_template_not_found(pay_tracker):
    new_template = EmailTemplate('New Reminder', 'Please pay your new invoice')
    with pytest.raises(ValueError):
        pay_tracker.edit_email_template('reminder', new_template)
