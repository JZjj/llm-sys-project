def is_balanced(s, pairs):
    """
    Check if the string s is balanced according to the given pairs of parentheses.

    Args:
        s (str): The input string to check.
        pairs (list of tuple): List of tuples where each tuple contains an opening and closing parenthesis.

    Returns:
        bool: True if s is balanced, False otherwise.
    """
    if not pairs:
        # No pairs defined, so string is balanced as there are no parentheses to match
        return True

    # Create dictionaries for quick lookup
    opening_to_closing = {opening: closing for opening, closing in pairs}
    closing_to_opening = {closing: opening for opening, closing in pairs}

    stack = []

    for char in s:
        if char in opening_to_closing:
            # It's an opening parenthesis, push to stack
            stack.append(char)
        elif char in closing_to_opening:
            # It's a closing parenthesis, check if matches last opening
            if not stack:
                return False
            last_open = stack.pop()
            if closing_to_opening[char] != last_open:
                return False
        else:
            # Ignore other characters
            continue

    # If stack is empty, all parentheses matched
    return not stack


if __name__ == "__main__":
    # Test cases to verify the implementation

    test_cases = [
        # (input_string, pairs, expected_result)
        ("{[()]}", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("{[(])}", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("abc(def)ghi", [('(', ')')], True),
        ("abc(def]ghi", [('(', ')'), ('[', ']')], False),
        ("", [('(', ')')], True),  # empty string
        ("abc", [('(', ')')], True),  # no parentheses
        ("[({})]", [('(', ')'), ('[', ']'), ('{', '}')], True),
        ("[({)}]", [('(', ')'), ('[', ']'), ('{', '}')], False),
        ("(]", [('(', ')'), ('[', ']')], False),
        ("(]", [], True),  # no pairs defined, so no parentheses to check
    ]

    for idx, (input_str, pairs, expected) in enumerate(test_cases, 1):
        result = is_balanced(input_str, pairs)
        print(f"Test case {idx}: {'PASS' if result == expected else 'FAIL'}")