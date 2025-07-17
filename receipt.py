"""
Represents a receipt for a collection of items.
"""

from decimal import Decimal
from typing import List
from .item import Item
from .calculator import TaxCalculator

class Receipt:
    """Manages a collection of items and calculates totals."""

    def __init__(self, tax_calculator: TaxCalculator):
        self._items: List[Item] = []
        self.tax_calculator = tax_calculator

    def add_item(self, item: Item):
        """Adds an item to the receipt and calculates its taxes."""
        item.sales_tax = self.tax_calculator.calculate_total_tax(item)
        item.total_price = item.price + item.sales_tax
        self._items.append(item)

    @property
    def items(self) -> List[Item]:
        """Returns the list of items on the receipt."""
        return self._items

    @property
    def total_sales_tax(self) -> Decimal:
        """Calculates the total sales tax for all items."""
        return sum(item.sales_tax for item in self._items)

    @property
    def total_amount(self) -> Decimal:
        """Calculates the grand total for all items."""
        return sum(item.total_price for item in self._items)

    def __str__(self) -> str:
        receipt_lines = []
        for item in self.items:
            receipt_lines.append(f"{item.quantity} {item.name}: {item.total_price:.2f}")
        receipt_lines.append(f"Sales Taxes: {self.total_sales_tax:.2f}")
        receipt_lines.append(f"Total: {self.total_amount:.2f}")
        return "\n".join(receipt_lines)
