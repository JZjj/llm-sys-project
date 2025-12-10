```python
def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)

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

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(input_str)
        print(f"Test case {i}: Input: {input_str!r}")
        print(f"Expected Output: {expected}")
        print(f"Actual Output:   {result}")
        print(f"Test {'PASSED' if result == expected else 'FAILED'}\n")


if __name__ == "__main__":
    main()
```