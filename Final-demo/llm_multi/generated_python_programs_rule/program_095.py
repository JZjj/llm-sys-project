```python
def is_balanced_brackets(s: str) -> bool:
    """
    Check if the brackets in the string s are balanced.
    Only brackets (), [], {} are considered; other characters ignored.

    Args:
        s (str): Input string possibly containing brackets.

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
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    return not stack


def main():
    test_cases = [
        ("([]{})", True),
        ("([)]", False),
        ("((()))", True),
        ("({[)]}", False),
        ("abc(def[ghi]{jkl})mno", True),
        ("", True),
        ("([{}])([]{})", True),
        ("([{])}", False),
        ("no brackets here", True),
        ("[({})](]", False),
    ]
    for s, expected in test_cases:
        result = is_balanced_brackets(s)
        print(f"Input: {s!r}\nBalanced: {result} (Expected: {expected})\n")


if __name__ == "__main__":
    main()
```