"""
Main entry point for the Aisle App CLI.
"""

import sys
from .parser import InputParser
from .receipt import Receipt
from .exceptions import AisleAppException

def main():
    """Reads shopping basket input, processes it, and prints the receipt."""
    print("Enter shopping basket items (one per line, empty line to finish):")

    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break

    if not lines:
        print("No items entered. Exiting.")
        return

    receipt = Receipt()
    try:
        for line in lines:
            item = InputParser.parse(line)
            receipt.add_item(item)
    except AisleAppException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print("\nOutput:")
    print(receipt)

if __name__ == "__main__":
    main()
