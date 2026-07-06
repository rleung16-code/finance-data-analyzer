import unittest
from analyzer import(
    calculate_total_income,
    calculate_total_expenses,
    calculate_net_cash_flow,
    summarize_expenses_by_category,
    find_largest_expense,
)
class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.transactions =  [
            {
                "date":"2026-07-01",
                "category": "Salary",
                "description": "Monthly salary",
                "amount": 25000.0,
                "type": "income",
            },
            {
                "date": "2026-07-02",
                "category": "Food",
                "description": "Lunch",
                "amount":65.0,
                "type": "expense",
            },
            {
                "date":"2026-07-03",
                "category": "Transport",
                "description": "MTR",
                "amount" :18.0,
                "type": "expense",
            },
            {
                "date": "2026-07-05",
                "category": "Rent",
                "description": "Apartment rent",
                "amount": 8000.0,
                "type": "expense",
            },
        ]
    def test_calculate_total_income(self):
        result = calculate_total_income(self.transactions)
        self.assertEqual(result, 25000.0)
    def test__calculate_total_expense(self):
        result = calculate_total_expenses(self.transactions)
        self.assertEqual(result, 8083.0)
    def test__calculate_net_cash_flow(self):
        result = calculate_net_cash_flow(self.transactions)
        self.assertEqual(result, 16917.0)
    def test__summarize_expenses_by_category(self):
        result = summarize_expenses_by_category(self.transactions)
        expected ={
            "Food": 65.0,
            "Transport": 18.0,
            "Rent": 8000.0,
        }
        self.assertEqual(result, expected)
    def test_find_largest_expense(self):
        result = find_largest_expense(self.transactions)
        self.assertEqual(result["category"], "Rent")
        self.assertEqual(result["amount"], 8000.0)
if __name__ == "__main__":
    unittest.main()