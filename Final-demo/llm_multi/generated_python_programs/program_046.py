```python
def longest_substring_with_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    max_length = 0
    char_freq = {}

    for right, right_char in enumerate(s):
        char_freq[right_char] = char_freq.get(right_char, 0) + 1

        while len(char_freq) > k:
            left_char = s[left]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            left += 1

        if len(char_freq) == k:
            max_length = max(max_length, right - left + 1)

    return max_length


def main():
    # Example test cases
    test_cases = [
        ("araaci", 2, 4),
        ("araaci", 1, 2),
        ("abcba", 2, 3),  # "bcb"
        ("aaabbb", 3, 0),  # no substring with 3 distinct chars
        ("aabbcc", 2, 4),  # "aabb", "bbcc"
        ("", 1, 0),  # empty string
        ("a", 1, 1),  # single character string
        ("eceba", 2, 3),  # "ece"
    ]

    for s, k, expected in test_cases:
        result = longest_substring_with_k_distinct(s, k)
        print(f"Input: s = '{s}', k = {k}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"{'PASS' if result == expected else 'FAIL'}\n")


if __name__ == "__main__":
    main()
```