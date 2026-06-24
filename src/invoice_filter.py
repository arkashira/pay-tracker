import dataclasses
from typing import List, Iterable, Optional

@dataclasses.dataclass(frozen=True)
class Invoice:
    id: int
    amount_due: float
    amount_paid: float

    @property
    def status(self) -> str:
        """Return payment status: 'Unpaid', 'Partially Paid', or 'Fully Paid'."""
        if self.amount_due == 0 and self.amount_paid >= 0:
            return "Fully Paid"
        if self.amount_paid == 0:
            return "Unpaid"
        if self.amount_paid < self.amount_due:
            return "Partially Paid"
        return "Fully Paid"

def filter_invoices(
    invoices: Iterable[Invoice], 
    *, 
    unpaid: bool = False, 
    partially_paid: bool = False, 
    fully_paid: bool = False, 
) -> List[Invoice]:
    """ 
    Filter invoices by payment status.

    Parameters
    ----------
    invoices : Iterable[Invoice]
        Collection of invoices to filter.
    unpaid : bool, optional
        Include invoices with status 'Unpaid'.
    partially_paid : bool, optional
        Include invoices with status 'Partially Paid'.
    fully_paid : bool, optional
        Include invoices with status 'Fully Paid'.

    Returns
    -------
    List[Invoice]
        List of invoices that match any of the selected filters.
    """
    if not any([unpaid, partially_paid, fully_paid]):
        raise ValueError("At least one filter must be selected")
    status_map = {
        "Unpaid": unpaid,
        "Partially Paid": partially_paid,
        "Fully Paid": fully_paid,
    }
    result = []
    for inv in invoices:
        if status_map.get(inv.status, False):
            result.append(inv)
    return result
