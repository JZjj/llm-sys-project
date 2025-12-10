```python
def length_of_longest_substring(s: str) -> int:
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
        ("a b c d e f g", 7),  # spaces included, longest substring without repeats is "a b c d"
        ("1234567890!@#$%^&*()", 20),  # all unique chars
        ("abba", 2),  # "ab" or "ba"
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(input_str)
        print(f"Test case #{i}: Input: {repr(input_str)}")
        print(f"Expected Output: {expected}")
        print(f"Actual Output:   {result}")
        print(f"Pass: {result == expected}")
        print("-" * 40)


if __name__ == "__main__":
    main()
```