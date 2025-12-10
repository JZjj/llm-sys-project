```python
#!/usr/bin/env python3
"""
A secure mathematical expression evaluator supporting +, -, *, / (integer division)
with correct operator precedence, without using eval() or external libraries.

Raises ValueError on malformed expressions or division by zero.
"""

import re

class ExpressionEvaluator:
    OPERATORS = {
        '+': (1, lambda a, b: a + b),
        '-': (1, lambda a, b: a - b),
        '*': (2, lambda a, b: a * b),
        '/': (2, lambda a, b: a // b),
    }

    @staticmethod
    def tokenize(expression: str):
        # Tokenize input string into integers and operators
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('OP',       r'[+\-*/]'),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
        for mo in re.finditer(tok_regex, expression):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                yield ('NUMBER', int(value))
            elif kind == 'OP':
                yield ('OP', value)
            elif kind == 'SKIP':
                continue
            else:
                raise ValueError(f"Invalid character in expression: {value}")

    @classmethod
    def parse(cls, tokens):
        """Parse tokens into Reverse Polish Notation (RPN) using Shunting Yard algorithm."""
        output_queue = []
        operator_stack = []

        prev_token_type = None
        for token_type, token_value in tokens:
            if token_type == 'NUMBER':
                output_queue.append(token_value)
                prev_token_type = 'NUMBER'
            elif token_type == 'OP':
                # Prevent expression starting with operator or two operators in a row
                if prev_token_type != 'NUMBER':
                    raise ValueError(f"Malformed expression: operator '{token_value}' cannot follow "
                                     f"'{prev_token_type or 'start'}'")
                while operator_stack:
                    top_op = operator_stack[-1]
                    if top_op not in cls.OPERATORS:
                        break
                    top_prec = cls.OPERATORS[top_op][0]
                    curr_prec = cls.OPERATORS[token_value][0]
                    if top_prec >= curr_prec:
                        output_queue.append(operator_stack.pop())
                    else:
                        break
                operator_stack.append(token_value)
                prev_token_type = 'OP'
            else:
                # Should not occur, just safety
                raise ValueError("Unknown token type")

        if prev_token_type == 'OP':
            raise ValueError("Malformed expression: ends with operator")

        while operator_stack:
            op = operator_stack.pop()
            if op not in cls.OPERATORS:
                raise ValueError("Malformed expression: invalid operator in stack")
            output_queue.append(op)

        return output_queue

    @classmethod
    def evaluate_rpn(cls, rpn):
        """Evaluate expression in Reverse Polish Notation."""
        stack = []
        for token in rpn:
            if isinstance(token, int):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Malformed expression: insufficient values for operation")
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    raise ValueError("Division by zero is not allowed")
                result = cls.OPERATORS[token][1](a, b)
                stack.append(result)
        if len(stack) != 1:
            raise ValueError("Malformed expression: leftover values after evaluation")
        return stack[0]

def evaluate_expression(expression: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers and +,-,*,/
    (integer division).
    Raises ValueError on invalid expressions or division by zero.
    """
    if not isinstance(expression, str):
        raise ValueError("Input expression must be a string")

    tokens = list(ExpressionEvaluator.tokenize(expression))
    if not tokens:
        raise ValueError("Empty expression")

    rpn = ExpressionEvaluator.parse(tokens)
    result = ExpressionEvaluator.evaluate_rpn(rpn)
    return result

def main():
    # Simple CLI interface for testing
    print("Enter a mathematical expression with non-negative integers and +, -, *, / (integer division).")
    print("Type 'exit' or press Ctrl+D to quit.")
    try:
        while True:
            try:
                expr = input('> ').strip()
            except EOFError:
                print()
                break
            if expr.lower() == 'exit':
                break
            if not expr:
                continue
            try:
                result = evaluate_expression(expr)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == '__main__':
    main()
```