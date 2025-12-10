```python
def check_balanced_parentheses_with_wildcards(s: str) -> bool:
    """
    Determines if the string s containing '(', ')', and '*'
    can be balanced by replacing '*' with '(', ')', or ''.

    Approach:
    Track the range of possible open parentheses counts:
      - '(' increases both min_open and max_open by 1
      - ')' decreases both min_open and max_open by 1
      - '*' can be '(', ')' or '', so min_open decreases by 1 (if '*'=>')'),
        max_open increases by 1 (if '*'=>'(')
    If max_open becomes negative at any point, return False.
    Clamp min_open to zero if it becomes negative.
    At the end, if min_open == 0, the string can be balanced.
    """
    min_open = 0
    max_open = 0

    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        else:  # char == '*'
            min_open -= 1
            max_open += 1

        if max_open < 0:
            return False
        if min_open < 0:
            min_open = 0

    return min_open == 0


def main():
    test_cases = [
        ("(*)", True),
        ("(*))", True),
        ("(()*", True),
        ("((*", False),
    ]

    for s, expected in test_cases:
        result = check_balanced_parentheses_with_wildcards(s)
        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}")
        print("-" * 20)


if __name__ == "__main__":
    main()
```