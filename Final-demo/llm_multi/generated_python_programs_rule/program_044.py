```python
import re
from typing import List, Union


class ExpressionEvaluator:
    """
    Safely parse and evaluate a mathematical expression containing non-negative integers
    and operators +, -, *, / with correct operator precedence.
    """

    # Allowed tokens regex pattern: numbers and operators
    TOKEN_PATTERN = re.compile(r'\s*(\d+|[+\-*/])\s*')

    def __init__(self, expression: str):
        self.expression = expression
        self.tokens: List[Union[str, int]] = []
        self.pos = 0

    def tokenize(self) -> None:
        """
        Tokenizes the input expression string into a list of tokens (ints and operator strings).
        Raises ValueError on invalid characters or empty expression.
        """
        if not self.expression or self.expression.strip() == "":
            raise ValueError("Empty expression is not allowed.")

        pos = 0
        tokens = []
        length = len(self.expression)

        while pos < length:
            match = self.TOKEN_PATTERN.match(self.expression, pos)
            if not match:
                # Invalid character encountered
                raise ValueError(f"Invalid character at position {pos}: '{self.expression[pos]}'")
            token = match.group(1)
            if token.isdigit():
                tokens.append(int(token))
            else:
                tokens.append(token)
            pos = match.end()

        if not tokens:
            raise ValueError("Expression contains no tokens.")
        self.tokens = tokens

    def parse(self) -> float:
        """
        Parses and evaluates the tokenized expression using recursive descent parsing.
        Returns the computed float result.
        """
        self.pos = 0
        value = self._parse_expression()
        if self.pos != len(self.tokens):
            # Extra tokens after valid expression
            raise ValueError(f"Unexpected token '{self.tokens[self.pos]}' at position {self.pos}")
        return float(value)

    def _parse_expression(self) -> float:
        """
        expression := term (( '+' | '-' ) term)*
        """
        value = self._parse_term()
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token == '+' or token == '-':
                self.pos += 1
                rhs = self._parse_term()
                if token == '+':
                    value += rhs
                else:
                    value -= rhs
            else:
                break
        return value

    def _parse_term(self) -> float:
        """
        term := factor (( '*' | '/' ) factor)*
        """
        value = self._parse_factor()
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token == '*' or token == '/':
                self.pos += 1
                rhs = self._parse_factor()
                if token == '*':
                    value *= rhs
                else:
                    if rhs == 0:
                        raise ValueError("Division by zero is not allowed.")
                    value /= rhs
            else:
                break
        return value

    def _parse_factor(self) -> float:
        """
        factor := NUMBER
        """
        if self.pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression; number expected.")

        token = self.tokens[self.pos]
        if isinstance(token, int):
            self.pos += 1
            return float(token)
        else:
            raise ValueError(f"Number expected but got '{token}' at position {self.pos}")


def evaluate_expression(expression: str) -> float:
    """
    Evaluates a mathematical expression string safely without using eval().
    Supports +, -, *, / with correct precedence.
    Raises ValueError on invalid input or division by zero.
    Returns result as float.
    """
    evaluator = ExpressionEvaluator(expression)
    evaluator.tokenize()
    result = evaluator.parse()
    return result


def main():
    import sys

    print("Enter a mathematical expression containing non-negative integers and +, -, *, / operators:")
    try:
        expr = input().strip()
        result = evaluate_expression(expr)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```