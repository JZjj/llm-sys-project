```python
#!/usr/bin/env python3
"""
Balanced Parentheses Validator with Error Position

This module provides a function to check whether the parentheses in a given string are balanced
and properly nested. It supports (), {}, and [] parentheses types. Non-parentheses characters are ignored.

Example usage:
    validate_parentheses("a(b[c]{d}e)f")  # Returns: True
    validate_parentheses("a(b[c]{d}e")   # Returns: (False, 1)
    validate_parentheses("a)b[c]{d}e")   # Returns: (False, 1)
"""

from typing import Union, Tuple


def validate_parentheses(s: str) -> Union[bool, Tuple[bool, int]]:
    """
    Check if the parentheses in the string `s` are balanced and properly nested.

    Only the following parentheses are considered: (), {}, [].
    All other characters are ignored.

    Returns:
        True if the string is balanced.
        Otherwise, returns a tuple (False, index) where `index` is the zero-based position
        of the first unmatched or misplaced parenthesis.

    Examples:
        >>> validate_parentheses("a(b[c]{d}e)f")
        True
        >>> validate_parentheses("a(b[c]{d}e")
        (False, 1)
        >>> validate_parentheses("a)b[c]{d}e")
        (False, 1)
    """
    opening = {'(': ')', '{': '}', '[': ']'}
    closing = {')', '}', ']'}
    stack = []  # stack of tuples: (opening_paren_char, index)

    for idx, ch in enumerate(s):
        if ch in opening:
            stack.append((ch, idx))
        elif ch in closing:
            if not stack:
                # Unmatched closing parenthesis
                return False, idx
            last_open, last_idx = stack.pop()
            if opening[last_open] != ch:
                # Mismatched closing parenthesis
                return False, idx

    if stack:
        # Unmatched opening parenthesis remains
        _, first_unmatched_idx = stack[0]
        return False, first_unmatched_idx

    return True


def _run_tests() -> None:
    # Basic tests to ensure correctness
    tests = [
        ("a(b[c]{d}e)f", True),
        ("a(b[c]{d}e", (False, 1)),
        ("a)b[c]{d}e", (False, 1)),
        ("", True),
        ("no parentheses", True),
        ("([{}])", True),
        ("([}{])", (False, 3)),
        (")(", (False, 0)),
        ("(((", (False, 0)),
        ("(()", (False, 0)),
        ("()[]{}", True),
        ("([)]", (False, 2)),
        ("{[(])}", (False, 4)),
        ("abc(def[ghi]{jkl}mno)pqr", True),
    ]

    all_passed = True
    for input_str, expected in tests:
        result = validate_parentheses(input_str)
        if result != expected:
            all_passed = False
            print(f"Test FAILED for input: {input_str!r}\n  Expected: {expected}\n  Got: {result}")
    if all_passed:
        print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
```