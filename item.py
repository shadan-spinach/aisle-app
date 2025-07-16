"""
Represents an item in the shopping basket.
"""

from decimal import Decimal, ROUND_HALF_UP

class Item:
    """Represents a single item in the shopping basket."""

    def __init__(self, name: str, price: Decimal, quantity: int, imported: bool):
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Item name must be a non-empty string.")
        if not isinstance(price, Decimal) or price < 0:
            raise TypeError("Item price must be a non-negative Decimal.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise TypeError("Item quantity must be a positive integer.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.imported = imported
        self.sales_tax = Decimal(0)
        self.total_price = self.price

    def __repr__(self) -> str:
        return f"Item(name='{self.name}', price={self.price}, quantity={self.quantity}, imported={self.imported})"
