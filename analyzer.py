import csv
from collections import defaultdict
from pathlib import Path

def load_transactions(file_path: str) -> list[dict]:
    """Load transactions from a CSV file."""
    path = Path (file_path)

    if not path.exists():
       raise FileNotFoundError(f"File not found: {file_path}")
    transactions = []

    with path.open("r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions 
def calculate_total_income(transactions: list[dict]) ->float:
    """Calculate total income"""
    return sum(item["amount"] for item in transactions if item["type"] == "income")

def calculate_total_expenses(transactions: list[dict]) ->float:
    """Calculate total expenses."""
    return sum(item["amount"] for item in transactions if item["type"] == "expense")
def calculate_net_cash_flow(transactions: list[dict]) -> float:
    """Calculate income minus expenses."""
    income = calculate_total_income(transactions)
    expenses = calculate_total_expenses(transactions)
    return income - expenses
def  summarize_expenses_by_category(transactions: list[dict]) -> dict[str, float]:
    """Summarize expenses by category."""
    category_totals = defaultdict(float)
    for item in transactions:
       if item["type"] == "expense":
           category_totals[item["category"]] += item["amount"]

    return dict(category_totals)
def find_largest_expense(transactions: list[dict]) -> dict | None:
    """Find the largest expense transaction."""
    expenses = [item for item in transactions if item["type"] == "expense"]
    if not expenses:
       return None
    return max(expenses, key=lambda item: item["amount"])