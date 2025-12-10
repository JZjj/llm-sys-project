```python
def longest_balanced_substring(s: str) -> int:
    pairs = {')': '(', '}': '{', ']': '['}
    stack = [-1]  # store indices, -1 as base for length calculation
    max_len = 0

    for i, ch in enumerate(s):
        if ch in '([{':
            stack.append(i)
        else:
            if stack and stack[-1] != -1 and s[stack[-1]] == pairs[ch]:
                stack.pop()
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
    return max_len


if __name__ == '__main__':
    tests = [
        ("()[{()}]", 8),
        (")({[)]}", 2),
        ("", 0),
        ("(((((", 0),
        ("()[]{}", 6),
        ("[({})]", 6),
        ("[({)}]", 2),
        ("()(()))", 6),
        ("[{()}]({[]})", 12),
        ("[({})](]", 6),
        (")))[[[]]](((", 6),
    ]

    for test_str, expected in tests:
        result = longest_balanced_substring(test_str)
        print(f"Input: {test_str!r} -> Output: {result} (Expected: {expected})")
        assert result == expected, f"Test failed for input {test_str!r}"
```