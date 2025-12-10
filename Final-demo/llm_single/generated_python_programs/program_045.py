def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Calculate the longest common subsequence (LCS) of two strings.
    The subsequence characters appear in the same order in both strings but are not necessarily contiguous.
    
    Args:
        str1 (str): First input string.
        str2 (str): Second input string.
        
    Returns:
        str: One of the longest common subsequences of str1 and str2.
        
    Raises:
        TypeError: If inputs are not strings.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
    
    len1, len2 = len(str1), len(str2)
    
    # Create a DP table with dimensions (len1+1) x (len2+1)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct one LCS from the DP table
    i, j = len1, len2
    lcs_chars = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_chars.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs_chars))


def main():
    # Example usage
    try:
        s1 = "AGGTAB"
        s2 = "GXTXAYB"
        result = longest_common_subsequence(s1, s2)
        print(f"Longest Common Subsequence of '{s1}' and '{s2}': '{result}'")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()