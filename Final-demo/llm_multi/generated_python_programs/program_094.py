```python
def longest_balanced_parentheses(s: str) -> int:
    """
    Returns the length of the longest balanced parentheses substring.
    """
    max_length = 0
    stack = [-1]  # stack to keep indices, initialized with -1 for base calculation

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length


def main():
    test_cases = [
        "(()())",
        ")()())",
        "(()",
        "",  # empty string
        "()()()()",
        "(((((((",
        ")))))))",
        "()(()))))(()()()()",
        "(()(()))())()(()())",
    ]

    for s in test_cases:
        print(f"Input: {s!r}")
        print(f"Output: {longest_balanced_parentheses(s)}")
        print('-' * 30)


if __name__ == "__main__":
    main()
```