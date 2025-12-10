```python
def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    char_index_map = {}
    max_length = 0
    start = 0  # Start index of current substring without duplicates

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
        ("abcdefg", 7),
        ("abba", 2),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: '{s}'")
        print(f"Expected Output: {expected}")
        print(f"Actual Output: {result}")
        print("-" * 30)


if __name__ == "__main__":
    main()
```