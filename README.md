# Aisle App - Sales Tax Calculator

Aisle App is a command-line application that calculates the total price for a shopping basket, including sales tax and import duties, and generates a formatted receipt.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Git

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

- `main.py`: The main entry point for the command-line application. It handles user input/output and orchestrates the application's flow.
- `parser.py`: Contains the `InputParser` class, which uses regular expressions to parse raw string input into structured `Item` objects.
- `item.py`: Defines the `Item` class, which serves as the data model for a single product, holding its name, price, quantity, and import status.
- `config.py`: A centralized module for all configuration settings like tax rates, rounding factors, and keywords for tax-exempt items. This makes adjustments easy without changing core logic.
- `calculator.py`: Holds the core business logic in the `TaxCalculator` class. It contains the algorithms for calculating sales tax and import duties.
- `receipt.py`: Defines the `Receipt` class, which manages the collection of all items. It calculates total taxes and the final grand total, and formats the final receipt for printing.
- `exceptions.py`: Contains custom exception classes (`AisleAppException`, `InvalidInputError`) for more specific and robust error handling.
- `tests/`: This directory holds all unit tests. `test_parser.py` validates the input parsing, and `test_calculator.py` verifies the tax calculation algorithms.
