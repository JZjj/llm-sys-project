def is_balanced_brackets(s: str, ignore_non_brackets: bool = False) -> bool:
    """
    Determines if the brackets in the string are balanced.
    
    Args:
        s (str): Input string containing brackets.
        ignore_non_brackets (bool): If True, ignore non-bracket characters.
    
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
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
        else:
            if not ignore_non_brackets:
                return False

    return not stack


if __name__ == "__main__":
    test_cases = [
        ("([]{})", True),
        ("([)]", False),
        ("((()))", True),
        ("[(])", False),
        ("", True),
        ("a(b)c[d]{e}", True),
        ("a(b]c", False),
    ]

    print("Testing without ignoring non-bracket characters:")
    for test_str, expected in test_cases[:5]:
        result = is_balanced_brackets(test_str)
        print(f"Input: {test_str!r}, Balanced: {result}, Expected: {expected}, Pass: {result == expected}")

    print("\nTesting with ignoring non-bracket characters:")
    for test_str, expected in test_cases:
        result = is_balanced_brackets(test_str, ignore_non_brackets=True)
        print(f"Input: {test_str!r}, Balanced: {result}, Expected: {expected}, Pass: {result == expected}")