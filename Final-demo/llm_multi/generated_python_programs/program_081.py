```python
def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    char_index_map = {}
    max_length = 0
    start = 0  # start index of current substring without duplicates

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
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
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("anviaj", 5),
        ("abc123!@#abc", 9),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: {s!r}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}")
        print("-" * 30)


if __name__ == "__main__":
    main()
```