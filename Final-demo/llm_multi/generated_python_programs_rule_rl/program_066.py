def are_brackets_balanced(s: str) -> bool:
    """
    Check if the brackets in the string are balanced.
    Considers (), [], and {} brackets only.
    Ignores all other characters.
    """
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
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
        "([]{})": True,
        "([)]": False,
        "((({[]})))": True,
        "[({})](]": False,
        "abc(def[ghi]{jkl})": True,
        "abc(def[ghi]{jkl}": False,
        "": True,
        "no brackets here": True,
        "([{}])(){}[]": True,
        "([{}])({[)]}": False,
    }

    for test_str, expected in test_cases.items():
        result = are_brackets_balanced(test_str)
        print(f"Input: {test_str!r} -> Balanced: {result} (Expected: {expected})")