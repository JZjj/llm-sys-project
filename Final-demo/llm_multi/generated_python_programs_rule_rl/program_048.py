def palindromic_substring_frequency(s):
    """
    Returns a dictionary mapping each unique palindromic substring (length >= 2)
    to the number of times it appears in the input string.
    """
    freq = {}
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            length = right - left + 1
            if length >= 2:
                substring = s[left:right+1]
                freq[substring] = freq.get(substring, 0) + 1
            left -= 1
            right += 1

    for i in range(n):
        expand_around_center(i, i)       # Odd length palindromes
        expand_around_center(i, i + 1)   # Even length palindromes

    return freq


if __name__ == "__main__":
    test_input = "ababa"
    result = palindromic_substring_frequency(test_input)
    print(result)  # Expected: {"aba": 2, "bab": 1, "ababa": 1}