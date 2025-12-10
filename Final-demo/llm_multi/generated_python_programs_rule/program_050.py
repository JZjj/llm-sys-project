```python
#!/usr/bin/env python3
"""
Find the longest substring without repeating characters.

Implements an O(n) time complexity solution using a sliding window approach.
"""

from typing import Optional


def find_longest_unique_substring(s: str) -> str:
    """
    Returns the longest substring of `s` without repeating characters.
    If multiple substrings have the same maximum length, returns the first one.

    :param s: Input string
    :return: Longest substring without repeating characters
    """
    if not s:
        return ""

    last_seen = {}
    start = 0
    max_len = 0
    max_start = 0

    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            max_start = start

    return s[max_start:max_start + max_len]


def main() -> None:
    # Example usage and simple test cases
    test_cases = [
        ("abcabcbb", "abc"),
        ("bbbbb", "b"),
        ("pwwkew", "wke"),
        ("", ""),
        ("abcdefg", "abcdefg"),
        ("aabcbcdbca", "cbda"),
        ("dvdf", "vdf"),
    ]

    for input_str, expected in test_cases:
        result = find_longest_unique_substring(input_str)
        print(f"Input: '{input_str}' -> Longest unique substring: '{result}'")
        assert result == expected, f"Test failed for input '{input_str}'"


if __name__ == "__main__":
    main()
```