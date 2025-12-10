```python
def evaluate_expression(expression: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers and the operators:
    +, -, *, / (integer division).
    The expression elements are space-separated.
    Operator precedence is respected: * and / before + and -, left-to-right within same precedence.

    Args:
        expression (str): The input expression string.

    Returns:
        int: The evaluated result.
    """
    # Tokenize by spaces
    tokens = expression.strip().split()

    if not tokens:
        raise ValueError("Empty expression")

    operators_set = {'+', '-', '*', '/'}

    # Validate tokens: even indices should be non-negative integers, odd indices should be operators
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not token.isdigit():
                raise ValueError(f"Expected non-negative integer at position {i}, got '{token}'")
        else:
            if token not in operators_set:
                raise ValueError(f"Expected operator at position {i}, got '{token}'")

    values = []
    ops = []

    def apply_op(a: int, b: int, op: str) -> int:
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a // b  # Integer division
        raise ValueError(f"Unsupported operator '{op}'")

    i = 0
    while i < len(tokens):
        if i % 2 == 0:
            values.append(int(tokens[i]))
            i += 1
        else:
            op = tokens[i]
            if op in ('*', '/'):
                if not values:
                    raise ValueError("Syntax error: operator at start")
                left = values.pop()
                right_token = tokens[i + 1]
                if not right_token.isdigit():
                    raise ValueError(f"Expected non-negative integer after operator at position {i}, got '{right_token}'")
                right = int(right_token)
                res = apply_op(left, right, op)
                values.append(res)
                i += 2
            else:
                ops.append(op)
                i += 1

    if len(values) != len(ops) + 1:
        raise ValueError("Syntax error: mismatch between numbers and operators")

    result = values[0]
    for idx, op in enumerate(ops):
        right = values[idx + 1]
        if op == '+':
            result += right
        elif op == '-':
            result -= right
        else:
            # This should never happen due to prior validation
            raise ValueError(f"Unexpected operator '{op}'")

    return result


def main():
    print("Enter a mathematical expression with non-negative integers and operators + - * / (integer division).")
    print("Tokens must be space-separated. Example: 3 + 5 * 2 - 4 / 2")
    try:
        expression = input("Expression: ").strip()
        if not expression:
            print("Empty input. Exiting.")
            return
        result = evaluate_expression(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```