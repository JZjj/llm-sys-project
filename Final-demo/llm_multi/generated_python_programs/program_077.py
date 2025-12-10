```python
def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            return False
    return not stack


if __name__ == "__main__":
    test_cases = [
        ("([]{})", True),
        ("([)]", False),
        ("((({[]})))", True),
        ("", True),
        ("[({})]", True),
        ("[({)}]", False),
        ("{[()()]}", True),
        ("{[(])}", False),
        ("{[", False),
        ("]", False),
    ]

    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(f"is_balanced({expr!r}) = {result} (Expected: {expected}) -> {'PASS' if result == expected else 'FAIL'}")
```