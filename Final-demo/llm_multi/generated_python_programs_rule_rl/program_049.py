def are_parentheses_balanced(s: str) -> bool:
    """
    Check if the parentheses in the string s are balanced and properly nested.
    Supports round (), square [], and curly {} parentheses.
    Ignores all other characters.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    test_cases = {
        "{[()()]}": True,
        "{[(])}": False,
        "No parentheses here!": True,
        "[(])": False,
        "([{}])": True,
    }

    for test_input, expected in test_cases.items():
        result = are_parentheses_balanced(test_input)
        print(f"Input: {test_input!r} -> Balanced: {result} (Expected: {expected})")