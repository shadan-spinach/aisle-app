"""
Calculates taxes for items in the shopping basket.
"""

from decimal import Decimal, ROUND_HALF_UP
from . import config
from .item import Item

def round_up_to_nearest_0_05(amount: Decimal) -> Decimal:
    """Rounds a decimal up to the nearest 0.05."""
    return (amount / Decimal(str(config.ROUNDING_FACTOR))).quantize(Decimal('1'), rounding=ROUND_HALF_UP) * Decimal(str(config.ROUNDING_FACTOR))

class TaxCalculator:
    """Calculates sales and import taxes for an item."""

    @staticmethod
    def is_exempt(item: Item) -> bool:
        """Checks if an item is exempt from sales tax."""
        return any(exempt_item in item.name.lower() for exempt_item in config.EXEMPT_ITEMS)

    @staticmethod
    def calculate_sales_tax(item: Item) -> Decimal:
        """Calculates the sales tax for a given item."""
        if TaxCalculator.is_exempt(item):
            return Decimal(0)
        tax = item.price * Decimal(str(config.SALES_TAX_RATE / 100.0))
        return round_up_to_nearest_0_05(tax)

    @staticmethod
    def calculate_import_duty(item: Item) -> Decimal:
        """Calculates the import duty for a given item."""
        if not item.imported:
            return Decimal(0)
        tax = item.price * Decimal(str(config.IMPORT_DUTY_RATE / 100.0))
        return round_up_to_nearest_0_05(tax)

    @staticmethod
    def calculate_total_tax(item: Item) -> Decimal:
        """Calculates the total tax for an item."""
        sales_tax = TaxCalculator.calculate_sales_tax(item)
        import_duty = TaxCalculator.calculate_import_duty(item)
        return sales_tax + import_duty
