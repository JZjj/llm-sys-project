def is_balanced_parentheses(s: str) -> bool:
    """
    Check if the input string has balanced and properly nested parentheses,
    considering round (), square [], and curly {} brackets.
    Non-parentheses characters are ignored.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if balanced and properly nested, False otherwise.
    """
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(bracket_pairs.values())
    stack = []

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    test_cases = {
        "([]{})": True,
        "([)]": False,
        "((()))": True,
        "({[}])": False,
        "abc(def[ghi]{jkl})": True,
        "": True,
        "(((((((((())))))))))": True,
        "[{()()}([])]": True,
        "[{(()}])": False,
        "no brackets here": True,
    }

    for test_str, expected in test_cases.items():
        result = is_balanced_parentheses(test_str)
        print(f"Input: {test_str!r} -> Balanced: {result} (Expected: {expected})")