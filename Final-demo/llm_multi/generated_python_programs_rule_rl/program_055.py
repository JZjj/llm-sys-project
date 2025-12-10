def is_valid_parentheses(s: str) -> bool:
    """
    Check if the input string of parentheses is valid.

    Args:
        s (str): The input string containing only '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False

    return not stack


if __name__ == "__main__":
    test_cases = {
        "()[]{}": True,
        "([{}])": True,
        "(]": False,
        "([)]": False,
        "((()": False,
        "": True,
        "[({})]": True,
        "[(])": False,
        "{[()]}": True,
        "}{": False,
        "([{}]))": False,
    }

    for test_input, expected in test_cases.items():
        result = is_valid_parentheses(test_input)
        print(f"Input: {test_input!r}, Expected: {expected}, Got: {result}, Result: {'PASS' if result == expected else 'FAIL'}")