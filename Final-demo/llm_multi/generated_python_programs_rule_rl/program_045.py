def is_balanced(s, pairs):
    """
    Check if the string s is balanced with respect to the given pairs of parentheses.

    :param s: Input string to check.
    :param pairs: List of tuples, each containing an opening and closing character.
    :return: True if balanced, False otherwise.
    """
    # Create dictionaries for quick lookup
    opening_chars = {opening for opening, _ in pairs}
    closing_to_opening = {closing: opening for opening, closing in pairs}

    stack = []

    for char in s:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_to_opening:
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        # Ignore characters not in any pair

    return not stack


if __name__ == "__main__":
    # Test cases to verify the function works as expected
    test_cases = [
        ("[{()}]", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("[{(])}", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("<abc>", [('<', '>')], True),
        ("<(])>", [('<', '>'), ('(', ')'), ('[', ']')], False),
        ("", [('(', ')')], True),  # Empty string is balanced
        ("abc", [('(', ')')], True),  # No parentheses, balanced
        ("([{}])", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("([}{])", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("<<>>", [('<', '>')], True),
        ("<><>", [('<', '>')], True),
        ("<><", [('<', '>')], False),
    ]

    for idx, (string, pairs, expected) in enumerate(test_cases, 1):
        result = is_balanced(string, pairs)
        print(f"Test case {idx}: {'PASS' if result == expected else 'FAIL'}")