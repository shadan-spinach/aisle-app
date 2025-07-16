"""
Parses input strings to create Item objects.
"""

import re
from decimal import Decimal
from .item import Item
from .exceptions import InvalidInputError

class InputParser:
    """Parses a line of input to extract item details."""

    # Regex to capture quantity, name, and price
    # e.g., "1 book at 12.49"
    ITEM_REGEX = re.compile(r"^(\d+)\s+(.+)\s+at\s+([\d.]+)$")

    @staticmethod
    def parse(line: str) -> Item:
        """Parses a single line of text into an Item object."""
        match = InputParser.ITEM_REGEX.match(line.strip())
        if not match:
            raise InvalidInputError(f"Invalid input format: '{line}'")

        quantity_str, name, price_str = match.groups()

        try:
            quantity = int(quantity_str)
            price = Decimal(price_str)
        except (ValueError, TypeError) as e:
            raise InvalidInputError(f"Invalid number format in '{line}'") from e

        imported = "imported" in name.lower()

        return Item(name=name, price=price, quantity=quantity, imported=imported)
