"""
Tests for the Receipt class.
"""

import unittest
from decimal import Decimal
from aisle_app.item import Item
from aisle_app.receipt import Receipt
from aisle_app.calculator import TaxCalculator

class TestReceipt(unittest.TestCase):

    def setUp(self):
        """Set up a standard tax calculator and receipt for tests."""
        self.calculator = TaxCalculator(
            sales_tax_rate=Decimal("10"),
            import_duty_rate=Decimal("5"),
            exempt_items=["book"]
        )
        self.receipt = Receipt(tax_calculator=self.calculator)

    def test_add_item_and_calculate_totals(self):
        book = Item(name="book", price=Decimal("10.00"), quantity=1, imported=False)
        cd = Item(name="music CD", price=Decimal("20.00"), quantity=1, imported=True)
        self.receipt.add_item(book) # Tax = 0
        self.receipt.add_item(cd) # Sales Tax = 2.00, Import Duty = 1.00
        self.assertEqual(self.receipt.total_sales_tax, Decimal("3.00"))
        self.assertEqual(self.receipt.total_amount, Decimal("10.00") + Decimal("23.00"))