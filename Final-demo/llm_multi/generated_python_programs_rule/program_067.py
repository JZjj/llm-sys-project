```python
import re
import sys
from typing import List, Tuple, Union

def evaluate_expression(expr: str) -> int:
    """
    Evaluates a mathematical expression string composed of non-negative integers and the
    operators +, -, *, and / (integer division) safely.

    Args:
        expr (str): The input expression string.

    Returns:
        int: The integer result of the evaluated expression.

    Raises:
        ValueError: If the expression contains invalid characters, is malformed,
                    or if division by zero occurs.
    """

    # Allowed characters: digits, whitespace, +, -, *, /
    if not re.fullmatch(r'[0-9+\-*/\s]+', expr):
        raise ValueError("Invalid characters in expression")

    tokens = tokenize(expr)
    if not tokens:
        raise ValueError("Empty expression")

    try:
        result, remaining = parse_expression(tokens, 0)
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except (IndexError, ValueError):
        raise ValueError("Malformed expression")

    if remaining != len(tokens):
        raise ValueError("Malformed expression")

    return result


def tokenize(expr: str) -> List[Union[int, str]]:
    """
    Tokenizes the expression into a list of integers and operator strings.

    Returns:
        List of tokens, where integer tokens are int and operators are str.
    """
    tokens: List[Union[int, str]] = []
    index = 0
    length = len(expr)

    while index < length:
        ch = expr[index]
        if ch.isspace():
            index += 1
            continue
        elif ch in '+-*/':
            tokens.append(ch)
            index += 1
        elif ch.isdigit():
            start = index
            while index < length and expr[index].isdigit():
                index += 1
            number_str = expr[start:index]
            tokens.append(int(number_str))
        else:
            # Should not happen due to regex check, but kept for safety
            raise ValueError("Invalid character found during tokenization")
    return tokens


def parse_expression(tokens: List[Union[int, str]], index: int) -> Tuple[int, int]:
    """
    Parses and evaluates an expression starting at tokens[index].
    Supports + and - operators.

    Returns:
        (result: int, next_index: int)
    """
    result, index = parse_term(tokens, index)

    while index < len(tokens):
        op = tokens[index]
        if op == '+' or op == '-':
            index += 1
            rhs, index = parse_term(tokens, index)
            if op == '+':
                result += rhs
            else:
                result -= rhs
        else:
            break
    return result, index


def parse_term(tokens: List[Union[int, str]], index: int) -> Tuple[int, int]:
    """
    Parses and evaluates a term starting at tokens[index].
    Supports * and / operators.

    Returns:
        (result: int, next_index: int)
    """
    result, index = parse_factor(tokens, index)

    while index < len(tokens):
        op = tokens[index]
        if op == '*' or op == '/':
            index += 1
            rhs, index = parse_factor(tokens, index)
            if op == '*':
                result *= rhs
            else:
                if rhs == 0:
                    raise ZeroDivisionError
                result //= rhs
        else:
            break
    return result, index


def parse_factor(tokens: List[Union[int, str]], index: int) -> Tuple[int, int]:
    """
    Parses a factor starting at tokens[index].
    A factor must be an integer.

    Returns:
        (int_value: int, next_index: int)
    """
    if index >= len(tokens):
        raise ValueError("Unexpected end of expression")

    token = tokens[index]
    if isinstance(token, int):
        return token, index + 1
    else:
        raise ValueError("Malformed expression: expected a number")


def main():
    print("Enter a mathematical expression with +, -, *, / (integer division).")
    print("Example: 12 + 3 * 4 - 6 / 2")
    try:
        expr = input("Expression: ")
        result = evaluate_expression(expr)
        print("Result:", result)
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)


if __name__ == "__main__":
    main()
```