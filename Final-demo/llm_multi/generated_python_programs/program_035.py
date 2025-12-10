```python
def is_balanced(s: str) -> bool:
    stack = []
    opening = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening[stack.pop()] != char:
                return False
    return not stack


if __name__ == "__main__":
    test_cases = [
        ("a*(b+c) - {d/[e*f]}", True),
        ("[(])", False),
        ("[({})]", True),
        ("[(])}", False),
        ("", True),
        ("no brackets here!", True),
        ("{[()()]}", True),
        ("{[(])}", False),
        ("{[}", False),
    ]

    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(f"is_balanced({expr!r}) = {result} (expected: {expected})")
        assert result == expected, f"Test failed for input: {expr}"
```