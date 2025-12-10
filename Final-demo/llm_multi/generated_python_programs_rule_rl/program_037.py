def is_balanced(s, pairs):
    """
    Check if the string s is balanced with respect to the given bracket pairs.

    Args:
        s (str): The input string containing various characters.
        pairs (list of tuple): List of tuples where each tuple contains two characters
                               representing an opening and a closing bracket.

    Returns:
        bool: True if the string is balanced according to the given pairs, False otherwise.
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
        {"s": "a(b[c]{d}e)f", "pairs": [('(', ')'), ('[', ']'), ('{', '}')], "expected": True},
        {"s": "a(b[c}d)e", "pairs": [('(', ')'), ('[', ']'), ('{', '}')], "expected": False},
        {"s": "<{[()]}>", "pairs": [('<', '>'), ('{', '}'), ('[', ']'), ('(', ')')], "expected": True},
        {"s": "abc", "pairs": [('(', ')')], "expected": True},
        {"s": "", "pairs": [('(', ')')], "expected": True},
        {"s": "([)]", "pairs": [('(', ')'), ('[', ']')], "expected": False},
        {"s": "<<>>", "pairs": [('<', '>')], "expected": True},
        {"s": "<<>", "pairs": [('<', '>')], "expected": False},
    ]

    for idx, case in enumerate(test_cases, 1):
        result = is_balanced(case["s"], case["pairs"])
        assert result == case["expected"], f"Test case {idx} failed: expected {case['expected']}, got {result}"
    print("All test cases passed.")