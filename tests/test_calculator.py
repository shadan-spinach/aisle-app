"""
Tests for the TaxCalculator.
"""


import unittest
from decimal import Decimal
from aisle_app.item import Item
from aisle_app.calculator import TaxCalculator


class TestTaxCalculator(unittest.TestCase):

    def setUp(self):
        """Create a TaxCalculator instance for testing."""
        self.calculator = TaxCalculator(
            sales_tax_rate=Decimal("10.0"),
            import_duty_rate=Decimal("5.0"),
            exempt_items=["book"]
        )


    def test_exempt_item_has_no_sales_tax(self):
        book = Item(name="book", price=Decimal("12.49"), quantity=1, imported=False)
        self.assertEqual(self.calculator.calculate_sales_tax(book), Decimal("0.00"))

    def test_non_exempt_item_has_sales_tax(self):
        cd = Item(name="music CD", price=Decimal("14.99"), quantity=1, imported=False)
        self.assertEqual(self.calculator.calculate_sales_tax(cd), Decimal("1.50"))

    def test_imported_item_has_import_duty(self):
        perfume = Item(name="imported bottle of perfume", price=Decimal("47.50"), quantity=1, imported=True)
        self.assertEqual(self.calculator.calculate_import_duty(perfume), Decimal("2.40"))

    def test_non_imported_item_has_no_import_duty(self):
        perfume = Item(name="bottle of perfume", price=Decimal("18.99"), quantity=1, imported=False)
        self.assertEqual(self.calculator.calculate_import_duty(perfume), Decimal("0.00"))

    def test_total_tax_for_imported_non_exempt_item(self):
        perfume = Item(name="imported bottle of perfume", price=Decimal("27.99"), quantity=1, imported=True)
        # Sales Tax: 2.80, Import Duty: 1.40
        self.assertEqual(self.calculator.calculate_total_tax(perfume), Decimal("4.20"))

if __name__ == '__main__':
    unittest.main()
