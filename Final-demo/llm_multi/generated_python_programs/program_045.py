```python
def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Args:
        s (str): Input string.

    Returns:
        int: Length of the longest substring with all unique characters.
    """
    char_index_map = {}
    longest = 0
    start = 0

    for i, ch in enumerate(s):
        if ch in char_index_map and char_index_map[ch] >= start:
            start = char_index_map[ch] + 1
        char_index_map[ch] = i
        longest = max(longest, i - start + 1)

    return longest


def main():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdefg", 7),
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: {s!r}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"{'PASS' if result == expected else 'FAIL'}")
        print("-" * 30)


if __name__ == "__main__":
    main()
```