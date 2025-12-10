```python
import re

class ExpressionEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('PLUS',     r'\+'),
            ('MINUS',    r'-'),
            ('MUL',      r'\*'),
            ('DIV',      r'/'),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('SPACE',    r'\s+'),
            ('MISMATCH', r'.'),
        ]
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        get_token = re.compile(tok_regex).match
        pos = 0
        tokens = []
        while pos < len(self.expression):
            m = get_token(self.expression, pos)
            if not m:
                raise ValueError(f"Invalid character at position {pos}")
            kind = m.lastgroup
            value = m.group(kind)
            if kind == 'NUMBER':
                tokens.append(('NUMBER', int(value)))
            elif kind in ('PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN'):
                tokens.append((kind, value))
            elif kind == 'SPACE':
                pass
            else:
                raise ValueError(f"Invalid character '{value}' at position {pos}")
            pos = m.end()
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type=None):
        token = self.peek()
        if token is None:
            if expected_type:
                raise ValueError(f"Expected token {expected_type} but got end of expression")
            return None
        if expected_type and token[0] != expected_type:
            raise ValueError(f"Expected token {expected_type} but got {token[0]} at position {self.pos}")
        self.pos += 1
        return token

    def parse(self):
        value = self.parse_expression()
        if self.peek() is not None:
            raise ValueError(f"Unexpected token '{self.peek()[1]}' at position {self.pos}")
        return value

    def parse_expression(self):
        value = self.parse_term()
        while True:
            token = self.peek()
            if token and token[0] in ('PLUS', 'MINUS'):
                op = token[0]
                self.consume()
                right = self.parse_term()
                if op == 'PLUS':
                    value += right
                else:
                    value -= right
            else:
                break
        return value

    def parse_term(self):
        value = self.parse_factor()
        while True:
            token = self.peek()
            if token and token[0] in ('MUL', 'DIV'):
                op = token[0]
                self.consume()
                right = self.parse_factor()
                if op == 'MUL':
                    value *= right
                else:
                    if right == 0:
                        raise ValueError("Division by zero")
                    value = value // right
            else:
                break
        return value

    def parse_factor(self):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return token[1]
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            value = self.parse_expression()
            if self.peek() is None or self.peek()[0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            self.consume('RPAREN')
            return value
        elif token[0] == 'MINUS':
            self.consume('MINUS')
            factor = self.parse_factor()
            return -factor
        else:
            raise ValueError(f"Unexpected token '{token[1]}' at position {self.pos}")

def evaluate_expression(expression: str) -> int:
    evaluator = ExpressionEvaluator(expression)
    evaluator.tokenize()
    return evaluator.parse()

def main():
    test_expr = "(2 + 3) * 4 - 5 / 2"
    try:
        result = evaluate_expression(test_expr)
        print(result)  # Expected output: 18
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```