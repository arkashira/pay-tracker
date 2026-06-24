import pytest
from invoice_filter import Invoice, filter_invoices

@pytest.fixture
def sample_invoices():
    return [
        Invoice(id=1, amount_due=100.0, amount_paid=0.0),  # Unpaid
        Invoice(id=2, amount_due=200.0, amount_paid=50.0),  # Partially Paid
        Invoice(id=3, amount_due=150.0, amount_paid=150.0),  # Fully Paid
        Invoice(id=4, amount_due=120.0, amount_paid=120.0),  # Fully Paid
        Invoice(id=5, amount_due=80.0, amount_paid=0.0),  # Unpaid
    ]

def test_filter_unpaid(sample_invoices):
    result = filter_invoices(sample_invoices, unpaid=True)
    assert len(result) == 2
    assert all(inv.status == "Unpaid" for inv in result)

def test_filter_partially_paid(sample_invoices):
    result = filter_invoices(sample_invoices, partially_paid=True)
    assert len(result) == 1
    assert result[0].id == 2
    assert result[0].status == "Partially Paid"

def test_filter_fully_paid(sample_invoices):
    result = filter_invoices(sample_invoices, fully_paid=True)
    assert len(result) == 2
    assert all(inv.status == "Fully Paid" for inv in result)

def test_filter_multiple(sample_invoices):
    result = filter_invoices(sample_invoices, unpaid=True, fully_paid=True)
    assert len(result) == 4
    ids = {inv.id for inv in result}
    assert ids == {1, 3, 4, 5}

def test_no_filters_raises():
    with pytest.raises(ValueError):
        filter_invoices(sample_invoices)

def test_edge_case_zero_amount_due():
    # Invoice with zero amount_due should be considered Fully Paid if amount_paid >= 0
    inv = Invoice(id=99, amount_due=0.0, amount_paid=0.0)
    result = filter_invoices([inv], fully_paid=True)
    assert result == [inv]
    assert inv.status == "Fully Paid"
