```python
import re
import sys

class ExpressionEvaluator:
    """
    Evaluates a mathematical expression string containing non-negative integers and operators:
    +, -, *, / (integer division).
    """

    # Allowed tokens: integers and operators
    TOKEN_REGEX = re.compile(r'\d+|[+\-*/]')
    VALID_CHAR_REGEX = re.compile(r'^[0-9+\-*/]+$')

    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = []
        self.pos = 0

    def validate_characters(self):
        # Only digits and +-*/ allowed, no spaces or other chars
        if not self.VALID_CHAR_REGEX.fullmatch(self.expression):
            raise ValueError("Expression contains invalid characters")

    def tokenize(self):
        self.tokens = self.TOKEN_REGEX.findall(self.expression)
        # After tokenization, check combined tokens equals original expression length
        if ''.join(self.tokens) != self.expression:
            raise ValueError("Malformed expression detected during tokenization")

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if expected is not None and token != expected:
            raise ValueError(f"Expected token '{expected}' but found '{token}'")
        self.pos += 1
        return token

    def parse(self):
        """
        Parses the expression with operator precedence:
        expr -> term ((+|-) term)*
        term -> factor ((*|/) factor)*
        factor -> integer
        """
        if not self.tokens:
            raise ValueError("Empty expression")
        result = self.parse_expr()
        if self.pos != len(self.tokens):
            raise ValueError("Malformed expression: extra tokens at the end")
        return result

    def parse_expr(self):
        result = self.parse_term()
        while True:
            op = self.peek()
            if op in ('+', '-'):
                self.consume()
                rhs = self.parse_term()
                if op == '+':
                    result = result + rhs
                else:
                    result = result - rhs
            else:
                break
        return result

    def parse_term(self):
        result = self.parse_factor()
        while True:
            op = self.peek()
            if op in ('*', '/'):
                self.consume()
                rhs = self.parse_factor()
                if op == '*':
                    result = result * rhs
                else:
                    if rhs == 0:
                        raise ValueError("Division by zero")
                    result = result // rhs  # integer division
            else:
                break
        return result

    def parse_factor(self):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if re.fullmatch(r'\d+', token):
            self.consume()
            # Leading zeros allowed per problem statement
            return int(token)
        else:
            raise ValueError(f"Unexpected token '{token}', expected integer")

def evaluate_expression(expr: str) -> int:
    evaluator = ExpressionEvaluator(expr)
    evaluator.validate_characters()
    evaluator.tokenize()
    return evaluator.parse()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 evaluator.py '<expression>'")
        print("Expression must contain non-negative integers and operators +, -, *, / (integer division) without spaces.")
        sys.exit(1)
    expression = sys.argv[1]
    try:
        result = evaluate_expression(expression)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```