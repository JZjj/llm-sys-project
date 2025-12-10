def longest_palindromic_substring(s: str) -> str:
    """
    Returns the longest palindromic substring in the input string s.
    If multiple substrings of the same maximum length exist, returns the first one.
    Case-sensitive and handles empty strings by returning an empty string.
    """
    if not s:
        return ""

    start, max_length = 0, 1
    n = len(s)

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1

    for i in range(n):
        left1, length1 = expand_around_center(i, i)
        if length1 > max_length:
            start, max_length = left1, length1

        left2, length2 = expand_around_center(i, i + 1)
        if length2 > max_length:
            start, max_length = left2, length2

    return s[start:start + max_length]


if __name__ == "__main__":
    test_cases = [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("", ""),
        ("a", "a"),
        ("ac", "a"),
        ("racecar", "racecar"),
        ("abacdfgdcaba", "aba"),
        ("abacdedcaba", "abacdedcaba"),
    ]

    for input_str, expected in test_cases:
        result = longest_palindromic_substring(input_str)
        print(f"Input: {input_str!r}")
        print(f"Output: {result!r}")
        print(f"Expected (one possible): {expected!r}")
        # Check if result length matches expected length and result appears first if lengths equal
        pass_condition = (
            result == expected or
            (len(result) == len(expected) and input_str.find(result) < input_str.find(expected))
        )
        print(f"Pass: {pass_condition}")
        print("-" * 40)