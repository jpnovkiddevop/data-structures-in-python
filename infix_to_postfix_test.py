import unittest
from infix_to_postfix import infix_to_postfix


class TestInfixToPostfix(unittest.TestCase):
    def test_infix_to_postfix(self):
        infix_expression = "a + b * c - ( d / e + f ) * g"
        expected_postfix_expression = "abc*+de/f+g*-"

        # Convert the infix expression to postfix
        actual_postfix_expression = infix_to_postfix(infix_expression)

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_postfix_expression,
                         expected_postfix_expression)


if __name__ == '__main__':
    unittest.main()
