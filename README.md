# Aisle App - Sales Tax Calculator

Aisle App is a command-line application that calculates the total price for a shopping basket, including sales tax and import duties, and generates a formatted receipt.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.6+
*   Git

### Cloning the Repository

To get a local copy of the project, clone the repository using the following command:

```bash
git clone <YOUR_REPOSITORY_URL>
```

## Running the Application

To run the application, execute the `main` module from the project's root directory. This ensures that all package imports are handled correctly.

```bash
python -m aisle-app.main
```

The application will then prompt you to enter your shopping basket items. After entering your items, provide an empty line (by pressing Enter) to signal the end of input.

## Running Tests

The project includes a suite of unit tests to ensure the core logic is working correctly. To run the tests, use Python's built-in `unittest` module from the project's root directory:

```bash
python -m unittest discover aisle-app
```

This command will automatically discover and run all tests within the `aisle-app/tests` directory.

## Sample Usage

The application accepts shopping basket items one per line. The format for each line is: `<quantity> <item name> at <price>`.

---

### **Sample Input 1**

```
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85
```

### **Corresponding Output 1**

```
Output:
1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83
```

---

### **Sample Input 2**

```
1 imported box of chocolates at 10.00
1 imported bottle of perfume at 47.50
```

### **Corresponding Output 2**

```
Output:
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15
```

---

## Project Structure

The project is organized as a Python package for modularity and scalability.

```
aisle-app/
└── aisle_app/
    ├── __init__.py
    ├── calculator.py
    ├── config.py
    ├── exceptions.py
    ├── item.py
    ├── main.py
    ├── parser.py
    ├── receipt.py
    └── tests/
        ├── __init__.py
        ├── test_calculator.py
        └── test_parser.py
```

## Module Explanations

*   `main.py`: The main entry point for the command-line application. It handles argument parsing, input/output, and orchestrates the application's flow. It uses `InputParser` to process input lines, `TaxCalculator` to calculate taxes, and `Receipt` to generate the final output.

*   `parser.py`: Contains the `InputParser` class, responsible for parsing raw string input (representing an item) into structured `Item` objects. It uses regular expressions to validate the input format and extract item details such as quantity, name, and price.

*   `item.py`: Defines the `Item` class, which serves as the data model for a single product. It stores essential information about an item, including its name, price, quantity, import status, calculated sales tax, and total price.

*   `config.py`: A centralized module for managing configuration settings. It defines constants for tax rates (`SALES_TAX_RATE`, `IMPORT_DUTY_RATE`), a list of keywords for tax-exempt items (`EXEMPT_ITEMS`), and the rounding factor (`ROUNDING_FACTOR`).

*   `calculator.py`: Contains the `TaxCalculator` class, which encapsulates the core tax calculation logic. It determines whether an item is tax-exempt and calculates sales tax and import duties based on the item's properties and the configuration settings.

*   `receipt.py`: Defines the `Receipt` class, which manages a collection of `Item` objects representing a shopping basket. It provides methods for adding items, calculating the total sales tax and the final grand total, and formatting the output as a human-readable receipt.

*   `exceptions.py`: Contains custom exception classes (`AisleAppException`, `InvalidInputError`) that provide more specific and robust error handling for various scenarios within the application.

*   `tests/`: This directory houses the unit tests for the application. `test_parser.py` validates the input parsing logic in `InputParser`, `test_calculator.py` verifies the tax calculation algorithms in `TaxCalculator`, and `test_receipt.py` ensures the correct calculation of totals and formatting of the receipt in the `Receipt` class.