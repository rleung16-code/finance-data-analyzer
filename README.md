# Finance Data Analyzer

A beginner-friendly python project that analyzes financial transaction data from a CSV file.

## Features
- Reads transaction data from a CSV file
- Calculate total income
- Calculate total expense
- Calculate net cash flow
- Summarize expenses by category
- Find the largest expense
- Include unit tests

## How to run

Run this command:

python main.py

## Run tests

Run this command:

python -m unittest discover -s tests -p test_*.py -v

##  Sample output

Total income: 27000.00
Total expense: 11,524.00
Net cash flow: 15,476.00

Laregest expense:
2026-07-05 | Rent |Apartment rent | 8,000.00

##  Project files


- analyzer.py
- main.py
- sample_transactions.csv
- tests/test_analyzer.py
- README.md
- .gitignore