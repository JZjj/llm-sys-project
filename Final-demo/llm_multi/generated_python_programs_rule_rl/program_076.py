def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in the input string.
    If multiple substrings have the same maximum length, returns the first one.
    """
    if not s:
        return ""

    start, max_length = 0, 1

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1

    for i in range(len(s)):
        left1, length1 = expand_around_center(i, i)
        left2, length2 = expand_around_center(i, i + 1)

        if length1 > max_length:
            start, max_length = left1, length1
        if length2 > max_length:
            start, max_length = left2, length2

    return s[start:start + max_length]


if __name__ == "__main__":
    test_input = "babad"
    result = longest_palindromic_substring(test_input)
    print(result)  # Expected output: "bab" (or "aba", but "bab" appears first)