```python
def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    :param s: input string
    :return: length of the longest substring without repeating characters
    """
    char_index_map = {}
    start = 0
    max_length = 0

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
        ("aab", 2),
        ("dvdf", 3),
        ("anviaj", 5),
        (" ", 1),
        ("abba", 2),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f'Input: "{s}"\nExpected Output: {expected}\nYour Output: {result}\n{"-"*30}')


if __name__ == "__main__":
    main()
```