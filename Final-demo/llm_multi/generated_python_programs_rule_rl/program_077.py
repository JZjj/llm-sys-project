def is_balanced_custom_pairs(s, pairs):
    """
    Check if the string s has balanced parentheses according to custom pairs.

    Args:
        s (str): The input string to check.
        pairs (list of tuple): List of (opening_char, closing_char) pairs.

    Returns:
        bool: True if balanced, False otherwise.
    """
    if not pairs:
        # No pairs means nothing to balance, so always True
        return True

    opening_chars = {op for op, _ in pairs}
    closing_to_opening = {cl: op for op, cl in pairs}

    stack = []

    for char in s:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_to_opening:
            if not stack:
                return False
            if stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        # Ignore characters not in pairs

    return not stack


if __name__ == "__main__":
    # Test cases to verify the function

    test_cases = [
        # Format: (pairs, string, expected_result)
        ([('(', ')'), ('{', '}')], "{()}", True),
        ([('(', ')'), ('{', '}')], "{(})", False),
        ([('a', 'b'), ('c', 'd')], "acdb", True),
        ([('a', 'b'), ('c', 'd')], "acbd", False),
        ([], "", True),  # No pairs, empty string
        ([], "anything", True),  # No pairs, non-empty string
        ([('<', '>')], "<abc><def>", True),
        ([('<', '>')], "<abc><def", False),
        ([('(', ')')], "", True),  # Empty string with pairs
        ([('(', ')')], "abc", True),  # No parentheses in string
    ]

    for idx, (pairs, string, expected) in enumerate(test_cases, 1):
        result = is_balanced_custom_pairs(string, pairs)
        print(f"Test case {idx}: is_balanced_custom_pairs({string!r}, {pairs}) -> {result} "
              f"{'PASS' if result == expected else 'FAIL'}")