from pay_tracker import PayTracker

def test_add_payment():
    pay_tracker = PayTracker([])
    pay_tracker.add_payment(100)
    assert pay_tracker.get_total() == 100

def test_get_total():
    pay_tracker = PayTracker([100, 200, 300])
    assert pay_tracker.get_total() == 600

def test_get_dashboard():
    pay_tracker = PayTracker([100, 200, 300])
    dashboard = pay_tracker.get_dashboard()
    assert dashboard["total"] == 600
    assert dashboard["payments"] == [100, 200, 300]

def test_empty_payments():
    pay_tracker = PayTracker([])
    assert pay_tracker.get_total() == 0
    assert pay_tracker.get_dashboard() == {"total": 0, "payments": []}
