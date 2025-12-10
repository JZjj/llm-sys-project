```python
def is_balanced_brackets(s: str) -> bool:
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    opening_brackets = set(bracket_pairs.values())
    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack


def main():
    test_cases = [
        ("{[()()]}", True),
        ("{[(])}", False),
        ("{{[[(())]]}}", True),
        ("abc{[()]}def", True),
        ("abc{[()]def}", False),
        ("", True),
        ("no brackets here", True),
        ("[({})](]", False),
    ]

    for s, expected in test_cases:
        result = is_balanced_brackets(s)
        print(f"Input: {s!r}")
        print(f"Balanced: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'PASSED' if result == expected else 'FAILED'}\n")


if __name__ == "__main__":
    main()
```