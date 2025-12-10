def is_balanced_parentheses(s: str) -> bool:
    """
    Check if the input string has balanced parentheses of types (), {}, and [].
    Non-bracket characters are ignored.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if balanced, False otherwise.
    """
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    opening_brackets = set(bracket_pairs.values())
    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack


if __name__ == "__main__":
    test_cases = {
        "{[()]}": True,
        "{[(])}": False,
        "{{[[(())]]}}": True,
        "([)]": False,
        "abc(def)[ghi]{jkl}": True,
        "(((())))": True,
        "(((()))": False,
        "": True,
        "no brackets here": True,
        "[{]}": False,
    }

    for test_input, expected in test_cases.items():
        result = is_balanced_parentheses(test_input)
        print(f"Input: {test_input!r} -> Balanced: {result} (Expected: {expected})")