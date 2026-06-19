import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class PayTracker:
    payments: list

    def add_payment(self, amount):
        self.payments.append(amount)

    def get_total(self):
        return sum(self.payments)

    def get_dashboard(self):
        total = self.get_total()
        payments = self.payments
        return {
            "total": total,
            "payments": payments
        }

def main():
    parser = ArgumentParser()
    parser.add_argument("--add", type=float, help="Add a payment")
    args = parser.parse_args()

    pay_tracker = PayTracker([])

    if args.add:
        pay_tracker.add_payment(args.add)

    dashboard = pay_tracker.get_dashboard()
    print(json.dumps(dashboard, indent=4))

if __name__ == "__main__":
    main()
