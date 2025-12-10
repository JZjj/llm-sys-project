import sys

def evaluate_expression(expr: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers and operators +, -, *, /.
    Operators follow standard precedence: * and / before + and -.
    Division is integer division.
    Raises ValueError for invalid expressions or division by zero.
    """
    if not expr:
        raise ValueError("Empty expression")

    allowed_chars = set("0123456789+-*/")
    if any(ch not in allowed_chars for ch in expr):
        raise ValueError("Expression contains invalid characters")

    tokens = []
    num_buffer = []
    for ch in expr:
        if ch.isdigit():
            num_buffer.append(ch)
        else:
            if not num_buffer:
                raise ValueError("Invalid expression syntax: operator without preceding number")
            tokens.append(int("".join(num_buffer)))
            num_buffer.clear()
            tokens.append(ch)
    if not num_buffer:
        raise ValueError("Expression cannot end with an operator")
    tokens.append(int("".join(num_buffer)))

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            if not isinstance(token, int):
                raise ValueError("Invalid expression syntax: expected number")
        else:
            if token not in "+-*/":
                raise ValueError("Invalid operator in expression")

    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, int):
            stack.append(token)
            i += 1
        else:
            if token in "*/":
                if not stack:
                    raise ValueError("Invalid expression syntax: operator at invalid position")
                left = stack.pop()
                if i + 1 >= len(tokens) or not isinstance(tokens[i + 1], int):
                    raise ValueError("Invalid expression syntax: operator not followed by number")
                right = tokens[i + 1]
                if token == "*":
                    result = left * right
                else:
                    if right == 0:
                        raise ValueError("Division by zero")
                    result = left // right
                stack.append(result)
                i += 2
            else:
                stack.append(token)
                i += 1

    result = None
    i = 0
    while i < len(stack):
        token = stack[i]
        if isinstance(token, int):
            if result is None:
                result = token
            else:
                raise ValueError("Invalid expression syntax: two numbers in a row without operator")
            i += 1
        else:
            if i + 1 >= len(stack) or not isinstance(stack[i + 1], int):
                raise ValueError("Invalid expression syntax: operator not followed by number")
            right = stack[i + 1]
            if token == "+":
                result += right
            else:
                result -= right
            i += 2

    if result is None:
        raise ValueError("Invalid expression syntax")

    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression = sys.argv[1]
    else:
        try:
            expression = input("Enter expression: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("No input provided")
            sys.exit(1)

    try:
        value = evaluate_expression(expression)
        print(value)
    except ValueError as e:
        print(f"Error: {e}")