def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Compute the longest common subsequence (LCS) between two strings.

    Parameters:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The longest common subsequence of str1 and str2.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")

    len1, len2 = len(str1), len(str2)

    # Create a 2D table to store lengths of LCS of substrings
    lcs_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Build the lcs_table from bottom up
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Backtrack to find the LCS string
    i, j = len1, len2
    lcs_chars = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_chars.append(str1[i - 1])
            i -= 1
            j -= 1
        elif lcs_table[i - 1][j] >= lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Since we traversed from the end, reverse to get the correct sequence
    lcs_chars.reverse()

    return ''.join(lcs_chars)


def main():
    """
    Example usage of longest_common_subsequence function.
    """
    try:
        # Example input strings
        str1 = "AGGTAB"
        str2 = "GXTXAYB"

        result = longest_common_subsequence(str1, str2)
        print(f"LCS of '{str1}' and '{str2}' is: '{result}'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()