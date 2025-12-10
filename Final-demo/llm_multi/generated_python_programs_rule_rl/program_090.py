import re

def evaluate_expression(expression: str) -> float:
    """
    Evaluate a mathematical expression containing non-negative integers,
    +, -, *, / operators, and parentheses.
    Returns the result as a float.
    Raises ValueError for invalid expressions or division by zero.
    """

    token_specification = [
        ('NUMBER',   r'\d+'),          # Integer number
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('LPAREN',   r'\('),           # Left Parenthesis
        ('RPAREN',   r'\)'),           # Right Parenthesis
        ('SPACE',    r'\s+'),          # Spaces (to skip)
        ('MISMATCH', r'.'),            # Any other character
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    get_token = re.compile(tok_regex).match

    tokens = []
    pos = 0
    length = len(expression)
    while pos < length:
        mo = get_token(expression, pos)
        if mo is None:
            raise ValueError(f"Invalid character {expression[pos]!r} in expression")
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value)))
        elif kind == 'OP':
            tokens.append(('OP', value))
        elif kind == 'LPAREN':
            tokens.append(('LPAREN', value))
        elif kind == 'RPAREN':
            tokens.append(('RPAREN', value))
        elif kind == 'SPACE':
            pass  # skip spaces
        elif kind == 'MISMATCH':
            raise ValueError(f"Invalid character {value!r} in expression")
        pos = mo.end()

    class Parser:
        def __init__(self, tokens):
            self.tokens = tokens
            self.pos = 0

        def current_token(self):
            return self.tokens[self.pos] if self.pos < len(self.tokens) else None

        def consume(self, expected_type=None, expected_value=None):
            token = self.current_token()
            if token is None:
                raise ValueError("Unexpected end of expression")
            if expected_type and token[0] != expected_type:
                raise ValueError(f"Expected token type {expected_type} but got {token[0]}")
            if expected_value and token[1] != expected_value:
                raise ValueError(f"Expected token value {expected_value} but got {token[1]}")
            self.pos += 1
            return token

        def parse_expr(self):
            result = self.parse_term()
            while True:
                token = self.current_token()
                if token and token[0] == 'OP' and token[1] in ('+', '-'):
                    op = token[1]
                    self.consume('OP')
                    rhs = self.parse_term()
                    if op == '+':
                        result += rhs
                    else:
                        result -= rhs
                else:
                    break
            return result

        def parse_term(self):
            result = self.parse_factor()
            while True:
                token = self.current_token()
                if token and token[0] == 'OP' and token[1] in ('*', '/'):
                    op = token[1]
                    self.consume('OP')
                    rhs = self.parse_factor()
                    if op == '*':
                        result *= rhs
                    else:
                        if rhs == 0:
                            raise ValueError("Division by zero")
                        result /= rhs
                else:
                    break
            return result

        def parse_factor(self):
            token = self.current_token()
            if token is None:
                raise ValueError("Unexpected end of expression")
            if token[0] == 'NUMBER':
                self.consume('NUMBER')
                return float(token[1])
            elif token[0] == 'LPAREN':
                self.consume('LPAREN')
                result = self.parse_expr()
                if self.current_token() is None or self.current_token()[0] != 'RPAREN':
                    raise ValueError("Mismatched parentheses")
                self.consume('RPAREN')
                return result
            else:
                raise ValueError(f"Unexpected token {token} in factor")

    parser = Parser(tokens)
    result = parser.parse_expr()
    if parser.current_token() is not None:
        raise ValueError("Unexpected token after complete parsing")
    return result


if __name__ == "__main__":
    import sys

    print("Enter a mathematical expression with non-negative integers, +, -, *, /, and parentheses.")
    print("Type 'exit' or Ctrl+C to quit.")
    while True:
        try:
            expr = input("Expression: ").strip()
            if expr.lower() == 'exit':
                break
            if not expr:
                continue
            value = evaluate_expression(expr)
            print(f"Result: {value}")
        except ValueError as e:
            print(f"Error: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            sys.exit(0)