def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in the input string.
    If multiple longest palindromes exist, returns the first one found.
    """
    if not s:
        return ""

    start, max_length = 0, 1

    def expand_around_center(left: int, right: int) -> (int, int):
        # Expand while the substring is a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the start index and length of the palindrome found
        return left + 1, right - left - 1

    for i in range(len(s)):
        # Odd length palindrome
        left1, length1 = expand_around_center(i, i)
        # Even length palindrome
        left2, length2 = expand_around_center(i, i + 1)

        # Check for the longer palindrome
        if length1 > max_length:
            start, max_length = left1, length1
        if length2 > max_length:
            start, max_length = left2, length2

    return s[start:start + max_length]


if __name__ == "__main__":
    import sys

    # Read input string safely from stdin
    input_str = sys.stdin.readline()
    if input_str:
        input_str = input_str.rstrip('\n')
    else:
        input_str = ""

    # Print the longest palindromic substring
    print(longest_palindromic_substring(input_str))