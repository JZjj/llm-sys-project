def longest_common_substring(s1: str, s2: str) -> str:
    """
    Finds the longest common substring between s1 and s2.
    If multiple substrings have the same maximum length,
    returns the one that appears first in s1.
    """
    if not s1 or not s2:
        return ""

    len_s1, len_s2 = len(s1), len(s2)
    dp = [0] * (len_s2 + 1)

    max_len = 0
    max_end_index_s1 = 0

    for i in range(1, len_s1 + 1):
        prev = 0
        for j in range(1, len_s2 + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev + 1
                if dp[j] > max_len:
                    max_len = dp[j]
                    max_end_index_s1 = i
                # If equal length found, do not update to keep first occurrence in s1
            else:
                dp[j] = 0
            prev = temp

    if max_len == 0:
        return ""
    return s1[max_end_index_s1 - max_len:max_end_index_s1]


if __name__ == "__main__":
    test_cases = [
        ("abcdef", "zcdemf", "cde"),
        ("abc", "def", ""),
        ("", "abc", ""),
        ("abc", "", ""),
        ("abcxyzabc", "xyzabcabc", "xyzabc"),
        ("aaaa", "aa", "aa"),
        ("abcde", "abfde", "de"),
        ("abc", "abc", "abc"),
    ]

    for idx, (s1, s2, expected) in enumerate(test_cases, 1):
        result = longest_common_substring(s1, s2)
        print(f"Test case {idx}: longest_common_substring({s1!r}, {s2!r}) = {result!r} "
              f"{'PASS' if result == expected else 'FAIL'}")