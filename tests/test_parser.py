"""
Tests for the InputParser.
"""

import unittest
from decimal import Decimal
from aisle_app.item import Item
from aisle_app.parser import InputParser
from aisle_app.exceptions import InvalidInputError

class TestInputParser(unittest.TestCase):

    def test_parse_valid_input(self):
        item = InputParser.parse("1 book at 12.49")
        self.assertEqual(item.quantity, 1)
        self.assertEqual(item.name, "book")
        self.assertEqual(item.price, Decimal("12.49"))
        self.assertFalse(item.imported)

    def test_parse_valid_imported_input(self):
        item = InputParser.parse("1 imported box of chocolates at 10.00")
        self.assertTrue(item.imported)

    def test_parse_invalid_input_format(self):
        with self.assertRaises(InvalidInputError):
            InputParser.parse("invalid input")

    def test_parse_invalid_number_format(self):
        with self.assertRaises(InvalidInputError):
            InputParser.parse("1 book at 12.49a")

if __name__ == '__main__':
    unittest.main()
