"""
Calculates taxes for items in the shopping basket.
"""

from decimal import Decimal, ROUND_HALF_UP
from .item import Item

def round_up_to_nearest_0_05(amount: Decimal) -> Decimal:
    """Rounds a decimal up to the nearest 0.05."""
    # A fixed rounding factor is generally acceptable as a global utility
    rounding_factor = Decimal("0.05")
    return (amount / rounding_factor).quantize(Decimal('1'), rounding=ROUND_HALF_UP) * rounding_factor

class TaxCalculator:
    """Calculates sales and import taxes for an item."""

    def __init__(self, sales_tax_rate: Decimal, import_duty_rate: Decimal, exempt_items: list[str]):
        self.sales_tax_rate = sales_tax_rate / 100
        self.import_duty_rate = import_duty_rate / 100
        self.exempt_items = exempt_items

    def is_exempt(self, item: Item) -> bool:
        """Checks if an item is exempt from sales tax."""
        return any(exempt_item in item.name.lower() for exempt_item in self.exempt_items)

    def calculate_sales_tax(self, item: Item) -> Decimal:
        """Calculates the sales tax for a given item."""
        if self.is_exempt(item):
            return Decimal(0)
        tax = item.price * self.sales_tax_rate
        return round_up_to_nearest_0_05(tax)

    def calculate_import_duty(self, item: Item) -> Decimal:
        """Calculates the import duty for a given item."""
        if not item.imported:
            return Decimal(0)
        tax = item.price * self.import_duty_rate
        return round_up_to_nearest_0_05(tax)

    def calculate_total_tax(self, item: Item) -> Decimal:
        """Calculates the total tax for an item."""
        sales_tax = self.calculate_sales_tax(item)
        import_duty = self.calculate_import_duty(item)
        return sales_tax + import_duty
