```python
def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    
    :param s: Input string consisting of ASCII characters
    :return: Length of the longest substring without repeated characters
    """
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
        
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)

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
        print(f'Input: "{s}"\nOutput: {result}\nExpected: {expected}\nResult: {"PASS" if result == expected else "FAIL"}\n')


if __name__ == "__main__":
    main()
```