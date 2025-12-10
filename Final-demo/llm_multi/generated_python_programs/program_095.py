```python
def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start, max_len = 0, 1

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd length palindrome
        l1, r1 = expand_around_center(i, i)
        length1 = r1 - l1 + 1
        if length1 > max_len:
            start = l1
            max_len = length1

        # Even length palindrome
        l2, r2 = expand_around_center(i, i + 1)
        length2 = r2 - l2 + 1
        if length2 > max_len:
            start = l2
            max_len = length2

    return s[start:start + max_len]


if __name__ == "__main__":
    test_str = "babad"
    print(longest_palindromic_substring(test_str))  # Expected: "bab" or "aba" but "bab" first
```