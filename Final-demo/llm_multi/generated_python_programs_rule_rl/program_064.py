def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in the input string s.
    The search is case-sensitive.
    If multiple substrings have the same maximum length, returns the first one.
    Returns an empty string if input is empty.
    """
    if not s:
        return ""

    start = 0
    max_length = 1  # A single character is always a palindrome

    def expand_around_center(left: int, right: int) -> (int, int):
        """
        Expands around the center indices left and right,
        returns the start index and length of the palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # After while loop ends, left and right are one step beyond palindrome bounds
        return left + 1, right - left - 1

    for i in range(len(s)):
        # Odd length palindrome
        left1, length1 = expand_around_center(i, i)
        if length1 > max_length:
            start = left1
            max_length = length1

        # Even length palindrome
        left2, length2 = expand_around_center(i, i + 1)
        if length2 > max_length:
            start = left2
            max_length = length2

    return s[start:start + max_length]


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ("babad", ["bab", "aba"]),  # both are valid, but "bab" appears first
        ("cbbd", ["bb"]),
        ("", [""]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("forgeeksskeegfor", ["geeksskeeg"]),
        ("abacdfgdcaba", ["aba"]),
        ("abacdfgdcabba", ["abba"]),
        ("abcde", ["a", "b", "c", "d", "e"]),
    ]

    for input_str, expected_list in test_cases:
        result = longest_palindromic_substring(input_str)
        # Check if result is in expected_list (to handle multiple valid answers)
        if result in expected_list:
            print(f"Input: {input_str!r} -> Output: {result!r} [PASS]")
        else:
            print(f"Input: {input_str!r} -> Output: {result!r} [FAIL] Expected one of {expected_list}")