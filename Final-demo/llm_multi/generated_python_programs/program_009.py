```python
def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    char_index_map = {}
    max_length = 0
    start = 0  # start index of current substring without repeats

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            # Found a repeating character inside current window
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length


def main():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdefg", 7),
        ("abba", 2),
        ("a1!a2@", 4),
        ("abcdefghijklmnopqrstuvwxyz0123456789", 36),
        ("dvdf", 3),
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