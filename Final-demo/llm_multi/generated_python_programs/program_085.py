```python
def longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    max_len = 0
    char_count = {}

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    # Example test cases
    print(longest_substring_k_distinct("eceba", 2))       # Expected output: 3 ("ece")
    print(longest_substring_k_distinct("aa", 1))          # Expected output: 2 ("aa")
    print(longest_substring_k_distinct("abcadcacacaca", 3))  # Expected output: 11 ("cadcacacaca")

    # Additional test cases
    print(longest_substring_k_distinct("", 1))            # Expected output: 0 (empty string)
    print(longest_substring_k_distinct("a", 0))           # Expected output: 0 (k=0)
    print(longest_substring_k_distinct("aabbcc", 1))      # Expected output: 2 ("aa", "bb", or "cc")
    print(longest_substring_k_distinct("aabbcc", 2))      # Expected output: 4 ("aabb" or "bbcc")
    print(longest_substring_k_distinct("aabbcc", 3))      # Expected output: 6 ("aabbcc")
```