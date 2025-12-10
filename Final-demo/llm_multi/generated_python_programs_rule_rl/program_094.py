def are_brackets_balanced(s: str) -> bool:
    """
    Check if the brackets in the string are balanced.
    Supports (), {}, [], and <> brackets.
    Non-bracket characters are ignored.
    """
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
    }
    opening_brackets = set(bracket_pairs.values())
    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack


if __name__ == "__main__":
    test_cases = {
        "{[()<>]}": True,
        "{[(<]>)}": False,
        "abc(123)[xyz]": True,
        "": True,
        "([{}<>])": True,
        "([}{])": False,
        "<{[()]}>": True,
        "<{[(])}>": False,
        "no brackets here": True,
        "(((())))": True,
        "(((()))": False,
    }

    for test_str, expected in test_cases.items():
        result = are_brackets_balanced(test_str)
        print(f"Input: {test_str!r}\nBalanced: {result}\nExpected: {expected}\n{'-'*30}")