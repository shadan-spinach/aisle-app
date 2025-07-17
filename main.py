"""
Main entry point for the Aisle App CLI.
"""
import argparse
import sys
from .parser import InputParser
from .receipt import Receipt
from .exceptions import AisleAppException
from .calculator import TaxCalculator
from . import config
from decimal import Decimal

def get_input_lines(input_file=None) -> list[str]:
    """Reads lines from a file or stdin."""
    if input_file:
        with open(input_file, 'r') as f:
            return f.readlines()
    else:
        print("Enter shopping basket items (one per line, empty line or EOF to finish):")
        lines = []
        while True:
            try:
                line = input()
                if not line:
                    break
                lines.append(line)
            except EOFError:
                break
        return lines

def main():
    """Reads shopping basket input, processes it, and prints the receipt."""
    parser = argparse.ArgumentParser(description="Calculate sales tax for a shopping basket.")
    parser.add_argument(
        "-f", "--file", dest="input_file",
        help="Path to a file containing basket items, one per line."
    )
    args = parser.parse_args()

    try:
        lines = get_input_lines(args.input_file)
    except FileNotFoundError:
        print(f"Error: Input file not found at '{args.input_file}'", file=sys.stderr)
        sys.exit(1)

    if not lines:
        print("No items entered. Exiting.")
        return

    # Create the calculator with rules from the config
    calculator = TaxCalculator(
        sales_tax_rate=Decimal(str(config.SALES_TAX_RATE)),
        import_duty_rate=Decimal(str(config.IMPORT_DUTY_RATE)),
        exempt_items=config.EXEMPT_ITEMS
    )
    receipt = Receipt(tax_calculator=calculator)
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            item = InputParser.parse(line)
            receipt.add_item(item)
        except AisleAppException as e:
            # Log error for the specific line and continue
            print(f"Warning: Skipping invalid line '{line}'. Reason: {e}", file=sys.stderr)

    print("\nOutput:")
    print(receipt)

if __name__ == "__main__":
    main()
