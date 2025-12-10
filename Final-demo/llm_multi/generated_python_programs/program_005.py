```python
def is_balanced_brackets(s: str) -> bool:
    """
    Check if the brackets in the string s are balanced.

    Args:
        s (str): Input string containing brackets and other characters.

    Returns:
        bool: True if brackets are balanced, False otherwise.
    """
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(bracket_pairs.values())

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    test_cases = {
        "([]{})": True,
        "([)]": False,
        "((()))": True,
        "({[)]}": False,
        "": True,
        "abc(123)[xyz]{foo}": True,
        "abc(123[x)yz]{foo}": False,
        "no brackets here": True,
    }

    for test_str, expected in test_cases.items():
        result = is_balanced_brackets(test_str)
        print(f"Input: {test_str!r:20} → Balanced? {result} (Expected: {expected})")
```