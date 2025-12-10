```python
def longest_substring_with_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s or k > len(s):
        return 0

    left = 0
    char_freq = {}
    max_length = 0

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


if __name__ == "__main__":
    # Test cases from the task description
    print(longest_substring_with_k_distinct("araaci", 2))  # Expected output: 4
    print(longest_substring_with_k_distinct("araaci", 1))  # Expected output: 2

    # Additional test cases
    print(longest_substring_with_k_distinct("araaci", 3))  # Expected output: 6 ("araaci")
    print(longest_substring_with_k_distinct("aabbcc", 1))  # Expected output: 2
    print(longest_substring_with_k_distinct("aabbcc", 2))  # Expected output: 4
    print(longest_substring_with_k_distinct("aabbcc", 3))  # Expected output: 6
    print(longest_substring_with_k_distinct("abcde", 5))   # Expected output: 5
    print(longest_substring_with_k_distinct("abcde", 6))   # Expected output: 0
```