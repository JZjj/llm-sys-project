def is_balanced(s, pairs):
    """
    Check if the string s has balanced brackets according to the custom pairs.

    Args:
        s (str): The input string containing brackets and other characters.
        pairs (list of tuple): List of tuples where each tuple is (opening, closing) bracket.

    Returns:
        bool: True if balanced, False otherwise.
    """
    opening_brackets = {opening for opening, _ in pairs}
    closing_brackets = {closing for _, closing in pairs}
    bracket_map = {closing: opening for opening, closing in pairs}

    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    test_cases = [
        ("[{()}]", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("[{(])}", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("", [('(', ')')], True),
        ("abc", [('(', ')')], True),
        ("([{}])", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("([}{])", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("<({[]})>", [('<', '>'), ('(', ')'), ('[', ']'), ('{', '}')], True),
        ("<({[)]}>", [('<', '>'), ('(', ')'), ('[', ']'), ('{', '}')], False),
    ]

    for i, (string, pairs, expected) in enumerate(test_cases, 1):
        result = is_balanced(string, pairs)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")