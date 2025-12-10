def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in the input string s.
    If multiple substrings have the same maximum length, returns the first one.
    The function is case-sensitive.
    """
    if not s:
        return ""

    start, max_length = 0, 1

    def expand_around_center(left: int, right: int) -> (int, int):
        """
        Expands around the given center and returns the start index and length
        of the palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # After the while loop, left and right are one step beyond the palindrome bounds
        return left + 1, right - left - 1

    for i in range(len(s)):
        # Odd length palindrome
        left1, length1 = expand_around_center(i, i)
        if length1 > max_length:
            start, max_length = left1, length1

        # Even length palindrome
        left2, length2 = expand_around_center(i, i + 1)
        if length2 > max_length:
            start, max_length = left2, length2

    return s[start:start + max_length]


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
        ("", ""),
        ("racecar", "racecar"),
        ("abacdfgdcaba", "aba"),
        ("abacdedcaba", "abacdedcaba"),
        ("123@#321", "123@#321"),
        ("Aa", "A"),
    ]

    for input_str, expected in test_cases:
        result = longest_palindromic_substring(input_str)
        print(f"Input: {input_str!r}")
        print(f"Output: {result!r}")
        print(f"Expected: {expected!r}")
        # Check if result is correct or an equally valid palindrome of same length appearing earlier
        valid = (
            result == expected or
            (len(result) == len(expected) and input_str.find(result) <= input_str.find(expected))
        )
        print(f"Pass: {valid}")
        print("-" * 40)