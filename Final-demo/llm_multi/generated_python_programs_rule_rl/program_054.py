def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in the input string s.
    The search is case-sensitive.
    If multiple substrings of the same maximum length exist, returns the first one found.
    """
    if not s:
        return ""

    start = 0
    max_length = 1

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        left1, right1 = expand_around_center(i, i)
        length1 = right1 - left1 + 1
        if length1 > max_length:
            start = left1
            max_length = length1

        left2, right2 = expand_around_center(i, i + 1)
        length2 = right2 - left2 + 1
        if length2 > max_length:
            start = left2
            max_length = length2

    return s[start:start + max_length]


if __name__ == "__main__":
    test_strings = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "forgeeksskeegfor",
        "",
        "Aa",
        "123@321",
        "abccba",
        "abacdfgdcaba"
    ]

    for test_str in test_strings:
        result = longest_palindromic_substring(test_str)
        print(f"Input: {test_str!r} -> Longest Palindromic Substring: {result!r}")