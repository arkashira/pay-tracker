from pay_tracker import PayTracker, Invoice, InvoiceStatus

def test_filter_invoices_all():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    filtered_invoices = pay_tracker.filter_invoices(InvoiceStatus.ALL)
    assert len(filtered_invoices) == 3

def test_filter_invoices_unpaid():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    filtered_invoices = pay_tracker.filter_invoices(InvoiceStatus.UNPAID)
    assert len(filtered_invoices) == 1

def test_filter_invoices_partially_paid():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    filtered_invoices = pay_tracker.filter_invoices(InvoiceStatus.PARTIALLY_PAID)
    assert len(filtered_invoices) == 1

def test_filter_invoices_paid():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    filtered_invoices = pay_tracker.filter_invoices(InvoiceStatus.PAID)
    assert len(filtered_invoices) == 1

def test_get_invoices_count_all():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    count = pay_tracker.get_invoices_count(InvoiceStatus.ALL)
    assert count == 3

def test_get_invoices_count_unpaid():
    invoices = [
        Invoice(1, "unpaid", 100, 0),
        Invoice(2, "partially_paid", 200, 50),
        Invoice(3, "paid", 300, 300)
    ]
    pay_tracker = PayTracker(invoices)
    count = pay_tracker.get_invoices_count(InvoiceStatus.UNPAID)
    assert count == 1
