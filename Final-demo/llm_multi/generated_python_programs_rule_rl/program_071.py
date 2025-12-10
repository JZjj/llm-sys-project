def check_balanced_brackets(s: str) -> bool:
    """
    Determine if the string s with '(', ')', and '*' can be balanced.
    '*' can be treated as '(', ')' or empty string.
    """

    low = 0  # minimum number of open '(' brackets possible
    high = 0  # maximum number of open '(' brackets possible

    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low = max(low - 1, 0)
            high -= 1
        else:  # char == '*'
            # '*' can be '(', ')' or empty
            low = max(low - 1, 0)  # treat '*' as ')', so low decreases
            high += 1  # treat '*' as '(' to increase high

        # If at any time, the max possible open brackets is negative, 
        # that means too many ')' than '(' even counting '*'.
        if high < 0:
            return False

    # If the minimum possible open brackets (low) is zero at the end,
    # that means the string can be balanced.
    return low == 0


if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        ("(*))", True),
        ("(*()", True),
        (")*(", False),
        ("", True),
        ("*()", True),
        ("((*))", True),
        ("(((******))", True),
        (")(", False),
        ("(*)", True),
        ("((*)", True),
        ("(*))((*", True),
    ]

    for s, expected in test_cases:
        result = check_balanced_brackets(s)
        print(f"Input: {s!r:10} Expected: {expected} Result: {result} {'PASS' if result == expected else 'FAIL'}")