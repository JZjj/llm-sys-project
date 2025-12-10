```python
def is_valid_parentheses(s: str) -> bool:
    """
    Check if the input string containing parentheses is valid.

    Args:
        s (str): String consisting of '(', ')', '{', '}', '[' and ']'

    Returns:
        bool: True if string is valid, False otherwise
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False

    return not stack


def main():
    test_cases = [
        ("()[]{}", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((((((", False),
        ("[{()}]", True),
        ("{[()()]}", True),
        ("{[(])}", False),
        ("[({})](]", False)
    ]

    for input_str, expected in test_cases:
        result = is_valid_parentheses(input_str)
        print(f"Input: {input_str!r} -> Output: {result} (Expected: {expected})")


if __name__ == "__main__":
    main()
```