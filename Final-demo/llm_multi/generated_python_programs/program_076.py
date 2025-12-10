```python
def longest_balanced_substring(s: str) -> int:
    max_length = 0
    stack = [-1]  # stack holds indices; starts with -1 to handle base case

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length


if __name__ == "__main__":
    # Example test
    test_input = ")()())"
    print(longest_balanced_substring(test_input))  # Expected output: 4

    # Additional tests
    assert longest_balanced_substring("") == 0
    assert longest_balanced_substring("()") == 2
    assert longest_balanced_substring("(()") == 2
    assert longest_balanced_substring(")()())()()(") == 4
    assert longest_balanced_substring("((()))") == 6
    assert longest_balanced_substring(")()(()))())(") == 6
```