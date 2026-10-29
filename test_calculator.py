
import unittest

from Calculator import evaluate_expression


class TestSmartCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression("2 + 3"), 5)

    def test_operator_precedence(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate_expression("(2 + 3) * 4"), 20)

    def test_negative_numbers(self):
        self.assertEqual(evaluate_expression("-5 + 2"), -3)

    def test_exponentiation(self):
        self.assertEqual(evaluate_expression("2 ** 3"), 8)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("10 / 0")

    def test_rejects_python_code(self):
        with self.assertRaises(ValueError):
            evaluate_expression("print(1)")

    def test_rejects_variable_names(self):
        with self.assertRaises(ValueError):
            evaluate_expression("abc + 2")


if __name__ == "__main__":
    unittest.main()
