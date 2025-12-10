def max_parentheses_depth(s: str) -> int:
    """
    Determine if the parentheses in the string are balanced.
    If balanced, return the maximum nesting depth.
    If not balanced, return -1.

    Args:
        s (str): Input string containing only '(' and ')'.

    Returns:
        int: Maximum nesting depth if balanced, else -1.
    """
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            current_depth -= 1
            if current_depth < 0:
                return -1
        else:
            return -1

    if current_depth != 0:
        return -1

    return max_depth


if __name__ == "__main__":
    test_cases = {
        "((()))": 3,
        "(()())": 2,
        "(()": -1,
        ")()(": -1,
        "": 0,
        "()()()": 1,
        "((())())": 3,
        "(((((((((())))))))))": 10,
        "())(()": -1,
    }

    for test_input, expected_output in test_cases.items():
        result = max_parentheses_depth(test_input)
        print(f"Input: {test_input!r}, Expected Output: {expected_output}, Actual Output: {result}, Test Passed: {result == expected_output}")