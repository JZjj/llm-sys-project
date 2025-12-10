```python
def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0  # Left pointer of the sliding window

    for end, char in enumerate(s):
        # If the character is already in the map and its index is inside the current window
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1  # Move start to right of the previous index of char

        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def main():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdefg", 7),
        ("abba", 2),
        ("dvdf", 3),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f'Input: "{s}"\nOutput: {result} (Expected: {expected})\n')


if __name__ == "__main__":
    main()
```