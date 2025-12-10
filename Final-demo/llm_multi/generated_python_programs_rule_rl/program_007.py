def is_balanced_parentheses(s: str) -> bool:
    """
    Check if the input string s containing parentheses is balanced.
    Supports (), {}, and [] brackets.

    Args:
        s (str): Input string containing only bracket characters.

    Returns:
        bool: True if balanced, False otherwise.
    """
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
        else:
            # Invalid character encountered; input should only contain brackets.
            return False

    return not stack


if __name__ == "__main__":
    test_cases = {
        "([]{})": True,
        "([)]": False,
        "((()": False,
        "": True,
        "(){}[]": True,
        "({[)]}": False,
        "([{}])": True,
        "[(])": False,
        "[({})](]": False,
        "(((((((((())))))))))": True,
    }

    for test_input, expected in test_cases.items():
        result = is_balanced_parentheses(test_input)
        print(f"Input: {test_input!r} -> Balanced: {result} (Expected: {expected})")