```python
import re

class ExpressionEvaluator:
    """
    A safe expression evaluator supporting +, -, *, /, parentheses and integer numbers.
    """

    def __init__(self, expression: str):
        self.expr = expression
        self.pos = 0
        self.length = len(expression)

    def parse(self):
        self._skip_whitespace()
        value = self._parse_expression()
        self._skip_whitespace()
        if self.pos != self.length:
            raise ValueError(f"Unexpected character at position {self.pos}: '{self.expr[self.pos]}'")
        return value

    def _skip_whitespace(self):
        while self.pos < self.length and self.expr[self.pos].isspace():
            self.pos += 1

    def _parse_expression(self):
        """
        expression := term (( '+' | '-' ) term)*
        """
        value = self._parse_term()
        while True:
            self._skip_whitespace()
            if self.pos >= self.length:
                break
            if self.expr[self.pos] == '+':
                self.pos += 1
                right = self._parse_term()
                value += right
            elif self.expr[self.pos] == '-':
                self.pos += 1
                right = self._parse_term()
                value -= right
            else:
                break
        return value

    def _parse_term(self):
        """
        term := factor ( ( '*' | '/' ) factor )*
        """
        value = self._parse_factor()
        while True:
            self._skip_whitespace()
            if self.pos >= self.length:
                break
            if self.expr[self.pos] == '*':
                self.pos += 1
                right = self._parse_factor()
                value *= right
            elif self.expr[self.pos] == '/':
                self.pos += 1
                right = self._parse_factor()
                if right == 0:
                    raise ValueError("Division by zero")
                value /= right
            else:
                break
        return value

    def _parse_factor(self):
        """
        factor := integer | '(' expression ')'
        """
        self._skip_whitespace()
        if self.pos >= self.length:
            raise ValueError("Unexpected end of expression")

        if self.expr[self.pos] == '(':
            self.pos += 1
            value = self._parse_expression()
            self._skip_whitespace()
            if self.pos >= self.length or self.expr[self.pos] != ')':
                raise ValueError(f"Expected ')' at position {self.pos}")
            self.pos += 1
            return value
        else:
            return self._parse_number()

    def _parse_number(self):
        """
        Parse an integer number (may include an optional leading '+' or '-').
        """
        self._skip_whitespace()
        start = self.pos

        # Optional leading + or -
        if self.pos < self.length and (self.expr[self.pos] == '+' or self.expr[self.pos] == '-'):
            self.pos += 1

        if self.pos >= self.length or not self.expr[self.pos].isdigit():
            raise ValueError(f"Expected number at position {self.pos}")

        while self.pos < self.length and self.expr[self.pos].isdigit():
            self.pos += 1

        num_str = self.expr[start:self.pos]
        # Validate with regex to ensure no invalid characters sneaked in
        if not re.fullmatch(r'[+-]?\d+', num_str):
            raise ValueError(f"Invalid number '{num_str}' at position {start}")

        return int(num_str)


def safe_evaluate(expression: str) -> float:
    """
    Safely evaluates a mathematical expression string containing integer numbers,
    +, -, *, / operators, and parentheses.

    :param expression: The input expression string.
    :return: The computed float result.
    :raises ValueError: If the expression is invalid or contains unsupported characters.
    """
    # Allowed characters check:
    # Only digits, whitespace, parentheses and operators + - * / are allowed.
    if not re.fullmatch(r'[0-9+\-*/()\s]+', expression):
        raise ValueError("Expression contains invalid characters")

    evaluator = ExpressionEvaluator(expression)
    result = evaluator.parse()
    # Result can be int or float; convert to float per requirements.
    return float(result)


def main():
    # Example usage
    examples = [
        "(2 + 3) * 4 - 5 / (1 + 1)",
        " 10 + 2 * 3 ",
        " ( 8 - 3 ) / 5 + 7 * (2 + 1) ",
        "42",
        "-5 + (3 * (2 - 8))",
    ]

    for expr in examples:
        try:
            result = safe_evaluate(expr)
            print(f"{expr} = {result}")
        except ValueError as e:
            print(f"Error evaluating '{expr}': {e}")

if __name__ == "__main__":
    main()
```