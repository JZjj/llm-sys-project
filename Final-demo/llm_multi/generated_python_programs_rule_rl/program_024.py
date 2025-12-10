import re

def evaluate_expressions(expressions):
    """
    Evaluate a list of mathematical expressions containing non-negative integers,
    '+' and '*' operators. Multiplication has higher precedence than addition.

    Args:
        expressions (list of str): List of expressions to evaluate.

    Returns:
        list of int: Evaluated results of the expressions.

    Raises:
        ValueError: If an expression is invalid or contains invalid characters.
    """
    results = []
    valid_pattern = re.compile(r'^[0-9+*]+$')

    for expr in expressions:
        if not isinstance(expr, str):
            raise ValueError(f"Expression must be a string, got {type(expr).__name__}")
        if not expr:
            raise ValueError("Expression cannot be empty")
        if not valid_pattern.fullmatch(expr):
            raise ValueError(f"Invalid characters in expression: '{expr}'")

        # Tokenize expression into numbers and operators
        tokens = []
        number_buffer = []
        for ch in expr:
            if ch.isdigit():
                number_buffer.append(ch)
            else:
                if not number_buffer:
                    raise ValueError(f"Operator '{ch}' cannot appear without a preceding number in expression: '{expr}'")
                tokens.append(int(''.join(number_buffer)))
                number_buffer.clear()
                tokens.append(ch)
        if not number_buffer:
            raise ValueError(f"Expression cannot end with an operator in expression: '{expr}'")
        tokens.append(int(''.join(number_buffer)))

        # Validate token sequence: must alternate number, operator, number, ...
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                if not isinstance(token, int):
                    raise ValueError(f"Expected number at position {i} in expression: '{expr}'")
            else:
                if token not in ('+', '*'):
                    raise ValueError(f"Invalid operator '{token}' at position {i} in expression: '{expr}'")

        # Evaluate multiplication first
        new_tokens = []
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], int):
                current_value = tokens[i]
                i += 1
                while i < len(tokens) and tokens[i] == '*':
                    i += 1
                    if i >= len(tokens) or not isinstance(tokens[i], int):
                        raise ValueError(f"Invalid syntax after '*' in expression: '{expr}'")
                    current_value *= tokens[i]
                    i += 1
                new_tokens.append(current_value)
            else:
                # Only '+' should appear here
                new_tokens.append(tokens[i])
                i += 1

        # Evaluate addition left to right
        result = new_tokens[0]
        i = 1
        while i < len(new_tokens):
            op = new_tokens[i]
            val = new_tokens[i + 1]
            if op == '+':
                result += val
            else:
                raise ValueError(f"Unexpected operator '{op}' in expression: '{expr}'")
            i += 2

        results.append(result)

    return results


if __name__ == "__main__":
    test_expressions = [
        "2+3*4",
        "10+20*30+40",
        "5*6+7*8",
        "123",
        "0+0*0",
    ]

    try:
        results = evaluate_expressions(test_expressions)
        for expr, res in zip(test_expressions, results):
            print(f"{expr} = {res}")
    except ValueError as e:
        print(f"Error: {e}")