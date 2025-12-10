import sys

def evaluate_expression(expression: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers,
    +, -, *, / (integer division), and parentheses.
    Raises ValueError if the expression is invalid.
    """
    INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
        'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
    )

    class Token:
        __slots__ = ('type', 'value')

        def __init__(self, type_, value=None):
            self.type = type_
            self.value = value

        def __repr__(self):
            return f"Token({self.type}, {repr(self.value)})"

    class Lexer:
        __slots__ = ('text', 'pos', 'current_char')

        def __init__(self, text):
            self.text = text
            self.pos = 0
            self.current_char = self.text[self.pos] if self.text else None

        def error(self):
            raise ValueError("Invalid character in expression")

        def advance(self):
            self.pos += 1
            self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

        def skip_whitespace(self):
            while self.current_char is not None and self.current_char.isspace():
                self.advance()

        def integer(self):
            result = []
            while self.current_char is not None and self.current_char.isdigit():
                result.append(self.current_char)
                self.advance()
            if not result:
                self.error()
            return int(''.join(result))

        def get_next_token(self):
            while self.current_char is not None:
                if self.current_char.isspace():
                    self.skip_whitespace()
                    continue
                if self.current_char.isdigit():
                    return Token(INTEGER, self.integer())
                if self.current_char == '+':
                    self.advance()
                    return Token(PLUS, '+')
                if self.current_char == '-':
                    self.advance()
                    return Token(MINUS, '-')
                if self.current_char == '*':
                    self.advance()
                    return Token(MUL, '*')
                if self.current_char == '/':
                    self.advance()
                    return Token(DIV, '/')
                if self.current_char == '(':
                    self.advance()
                    return Token(LPAREN, '(')
                if self.current_char == ')':
                    self.advance()
                    return Token(RPAREN, ')')
                self.error()
            return Token(EOF, None)

    class Parser:
        __slots__ = ('lexer', 'current_token')

        def __init__(self, lexer):
            self.lexer = lexer
            self.current_token = self.lexer.get_next_token()

        def error(self, message="Invalid syntax"):
            raise ValueError(message)

        def eat(self, token_type):
            if self.current_token.type == token_type:
                self.current_token = self.lexer.get_next_token()
            else:
                self.error(f"Expected token {token_type} but got {self.current_token.type}")

        def factor(self):
            """
            factor : INTEGER | LPAREN expr RPAREN
            """
            token = self.current_token
            if token.type == INTEGER:
                self.eat(INTEGER)
                return token.value
            elif token.type == LPAREN:
                self.eat(LPAREN)
                result = self.expr()
                if self.current_token.type != RPAREN:
                    self.error("Mismatched parentheses")
                self.eat(RPAREN)
                return result
            else:
                self.error("Expected integer or '('")

        def term(self):
            """
            term : factor ((MUL | DIV) factor)*
            """
            result = self.factor()
            while self.current_token.type in (MUL, DIV):
                token = self.current_token
                if token.type == MUL:
                    self.eat(MUL)
                    right = self.factor()
                    result = result * right
                elif token.type == DIV:
                    self.eat(DIV)
                    right = self.factor()
                    if right == 0:
                        raise ValueError("Division by zero")
                    result = result // right  # Integer division
            return result

        def expr(self):
            """
            expr : term ((PLUS | MINUS) term)*
            """
            result = self.term()
            while self.current_token.type in (PLUS, MINUS):
                token = self.current_token
                if token.type == PLUS:
                    self.eat(PLUS)
                    right = self.term()
                    result = result + right
                elif token.type == MINUS:
                    self.eat(MINUS)
                    right = self.term()
                    result = result - right
            return result

        def parse(self):
            result = self.expr()
            if self.current_token.type != EOF:
                self.error("Unexpected characters at end of expression")
            return result

    if not isinstance(expression, str):
        raise ValueError("Expression must be a string")

    lexer = Lexer(expression)
    parser = Parser(lexer)
    return parser.parse()


if __name__ == "__main__":
    print("Enter a mathematical expression with non-negative integers, +, -, *, /, and parentheses.")
    print("Type 'exit' or press Ctrl+C to quit.")
    try:
        while True:
            try:
                expr = input(">>> ").strip()
                if expr.lower() == 'exit':
                    break
                if not expr:
                    continue
                result = evaluate_expression(expr)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
            except EOFError:
                break
    except KeyboardInterrupt:
        print("\nExiting.")