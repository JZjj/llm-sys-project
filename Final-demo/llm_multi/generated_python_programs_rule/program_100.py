```python
import re
from typing import List, Union


class ExpressionEvaluator:
    """
    Class to tokenize and evaluate mathematical expressions
    supporting +, -, *, /, parentheses, and non-negative integers.
    """

    # Allowed tokens regex pattern (numbers, operators, parentheses, whitespace)
    TOKEN_PATTERN = re.compile(r'\s*(?:(\d+)|(.))')

    def __init__(self, expression: str):
        self.expression = expression
        self.tokens: List[Union[str, int]] = []
        self.pos = 0

    def tokenize(self):
        """
        Converts the expression string into a list of tokens (numbers and operators).
        Raises ValueError on unsupported characters or empty expressions.
        """
        tokens = []
        idx = 0
        length = len(self.expression)

        while idx < length:
            match = self.TOKEN_PATTERN.match(self.expression, idx)
            if not match:
                # No valid token found, invalid character likely
                raise ValueError(f"Invalid character at position {idx}")

            number, operator = match.groups()
            if number is not None:
                # Valid number token
                tokens.append(int(number))
            elif operator in '+-*/()':
                tokens.append(operator)
            elif operator.strip() == '':
                # whitespace, skip
                pass
            else:
                raise ValueError(f"Unsupported character '{operator}' at position {idx}")

            idx = match.end()

        if not tokens:
            raise ValueError("Empty expression")

        self.tokens = tokens

    def peek(self):
        """Return current token without consuming it."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        """
        Consume and return the current token and advance position.
        If expected is provided, verifies the current token matches it.
        """
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if expected is not None and token != expected:
            raise ValueError(f"Expected '{expected}' but got '{token}'")
        self.pos += 1
        return token

    def parse(self) -> float:
        """
        Parse the tokens and evaluate the expression using recursive descent parsing.
        Implements operator precedence and parentheses.
        Expression grammar:
            expr    := term (( '+' | '-' ) term)*
            term    := factor (( '*' | '/' ) factor)*
            factor  := NUMBER | '(' expr ')'
        Returns:
            float: computed result
        Raises:
            ValueError: on invalid syntax or division by zero.
        """
        result = self.parse_expr()

        if self.pos != len(self.tokens):
            raise ValueError("Unexpected token after complete expression")

        return float(result)

    def parse_expr(self) -> float:
        """Parse addition and subtraction."""
        result = self.parse_term()

        while True:
            token = self.peek()
            if token == '+':
                self.consume('+')
                rhs = self.parse_term()
                result += rhs
            elif token == '-':
                self.consume('-')
                rhs = self.parse_term()
                result -= rhs
            else:
                break
        return result

    def parse_term(self) -> float:
        """Parse multiplication and division."""
        result = self.parse_factor()

        while True:
            token = self.peek()
            if token == '*':
                self.consume('*')
                rhs = self.parse_factor()
                result *= rhs
            elif token == '/':
                self.consume('/')
                rhs = self.parse_factor()
                if rhs == 0:
                    raise ValueError("Division by zero")
                result /= rhs
            else:
                break
        return result

    def parse_factor(self) -> float:
        """Parse numbers and parenthesized expressions."""
        token = self.peek()

        if isinstance(token, int):
            self.consume()
            return float(token)
        elif token == '(':
            self.consume('(')
            result = self.parse_expr()
            self.consume(')')
            return result
        else:
            raise ValueError(f"Unexpected token '{token}' in factor")


def safe_eval(expression: str) -> float:
    """
    Safely evaluate a mathematical expression string consisting of non-negative integers,
    operators (+, -, *, /), and parentheses.

    Parameters:
        expression (str): The expression to evaluate.

    Returns:
        float: The numerical result of the expression.

    Raises:
        ValueError: If the expression is invalid or contains unsupported characters.
    """
    evaluator = ExpressionEvaluator(expression)
    evaluator.tokenize()
    result = evaluator.parse()
    return result


def main():
    # Basic demonstration and manual tests
    test_expressions = [
        "2 + 3 * 4",           # 14.0
        " ( 2 + 3 ) * 4 ",     # 20.0
        "10 / 2 + 3",          # 8.0
        "10 / (5 - 5)",        # Division by zero error
        "42",                  # 42.0
        "3 + 4 * 2 / (1 - 5)", # 1.0
        "3 +",                 # Invalid syntax error
        "2 + 2a",              # Invalid character error
        "  ",                  # Invalid syntax error (empty)
    ]

    for expr in test_expressions:
        try:
            result = safe_eval(expr)
            print(f"Expression: {expr!r} => Result: {result}")
        except ValueError as e:
            print(f"Expression: {expr!r} => Error: {e}")


if __name__ == "__main__":
    main()
```