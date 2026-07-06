from analyzer import (
    load_transactions,
    calculate_total_income,
    calculate_total_expenses,
    calculate_net_cash_flow,
    summarize_expenses_by_category,
    find_largest_expense,
)
def main() -> None:
    file_path = "sample_transactions.csv"
    transactions = load_transactions(file_path)
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    net_cash_flow = calculate_net_cash_flow(transactions)
    category_summary = summarize_expenses_by_category(transactions)
    largest_expense = find_largest_expense(transactions)
    print("Finance Data Analyzer")
    print("-" * 30)
    print(f"Total income:{total_income:,.2f}")
    print(f"Total expense:{total_expenses:,.2f}")
    print(f"Net cash flow:{net_cash_flow:,.2f}")

    print("\nExpenses by category:")
    for category, amount in category_summary.items():
        print(f"-{category}:{amount:,.2f}")
    print("\nLargest expense:")
    if largest_expense:
       print(
            f"{largest_expense['date']} | "
            f"{largest_expense['category']} | "
            f"{largest_expense['description']} | "
            f"{largest_expense['amount']:,.2f}"
        )
    else:
        print("No expense found.") 

if __name__== "__main__":
    main()