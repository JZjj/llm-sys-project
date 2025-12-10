import sys

def evaluate_expression(expr: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers and the operators
    +, -, *, / (integer division), without parentheses or spaces.
    Operator precedence is respected: * and / before + and -, evaluated left to right.
    
    Args:
        expr (str): The expression string to evaluate.
        
    Returns:
        int: The evaluated integer result.
        
    Raises:
        ValueError: If the expression is invalid or division by zero occurs.
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
                raise ValueError("Malformed expression: operator without preceding number")
            tokens.append(int("".join(num_buffer)))
            num_buffer.clear()
            tokens.append(ch)

    if not num_buffer:
        raise ValueError("Malformed expression: ends with operator")
    tokens.append(int("".join(num_buffer)))

    # First pass: handle * and / left to right
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
                    raise ValueError("Malformed expression: operator without left operand")
                if i + 1 >= len(tokens) or not isinstance(tokens[i+1], int):
                    raise ValueError("Malformed expression: operator without right operand")
                left = stack.pop()
                right = tokens[i+1]
                if token == "*":
                    result = left * right
                else:  # token == "/"
                    if right == 0:
                        raise ValueError("Division by zero")
                    result = left // right
                stack.append(result)
                i += 2
            else:
                stack.append(token)
                i += 1

    # Second pass: handle + and - left to right
    result = None
    i = 0
    while i < len(stack):
        token = stack[i]
        if isinstance(token, int):
            if result is None:
                result = token
            else:
                # Two consecutive numbers without operator
                raise ValueError("Malformed expression: two consecutive numbers")
            i += 1
        else:
            if i + 1 >= len(stack) or not isinstance(stack[i+1], int):
                raise ValueError("Malformed expression: operator without right operand")
            right = stack[i+1]
            if token == "+":
                result += right
            else:  # token == "-"
                result -= right
            i += 2

    if result is None:
        raise ValueError("Malformed expression: no numbers found")

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 evaluate_expression.py '<expression>'")
        sys.exit(1)
    expression = sys.argv[1]
    try:
        value = evaluate_expression(expression)
        print(value)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)