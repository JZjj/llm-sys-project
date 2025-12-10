def check_balanced_with_wildcards(s: str) -> bool:
    """
    Check if the string s containing '(', ')', and '*' is balanced.
    '*' can represent '(', ')' or empty string.
    """
    if not s:
        # Empty string is not balanced as per problem constraints (length >= 1)
        return False

    low = 0  # minimum number of open '(' needed
    high = 0  # maximum number of open '(' possible

    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low = max(low - 1, 0)
            high -= 1
            if high < 0:
                # More ')' than '(' and '*' combined
                return False
        elif char == '*':
            # '*' can be '(', ')' or empty
            low = max(low - 1, 0)  # if '*' is ')'
            high += 1  # if '*' is '('
        else:
            # Invalid character found, return False for safety
            return False

    return low == 0


if __name__ == "__main__":
    # Test cases to verify correctness
    test_cases = {
        "(*)": True,
        "(*))": True,
        "((*": False,
        "": False,  # empty string is not balanced as per problem constraints (length >=1)
        "*": True,
        "((*)": True,
        "(()*": True,
        ")*(": False,
        "((*)*)": True,
        "(((******))": True,
        "(((******)))": True,
        "(((******))))": False,
    }

    for test_input, expected in test_cases.items():
        result = check_balanced_with_wildcards(test_input)
        print(f"Input: {test_input!r}, Balanced: {result}, Expected: {expected}, Pass: {result == expected}")