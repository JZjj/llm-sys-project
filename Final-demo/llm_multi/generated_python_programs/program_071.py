```python
def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        left1, right1 = expand_around_center(i, i)
        left2, right2 = expand_around_center(i, i + 1)

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]


if __name__ == "__main__":
    test_inputs = [
        "babad",
        "cbbd",
        "",
        "a",
        "ac",
        "forgeeksskeegfor",
        "abacdfgdcaba",
        "abacdfgdcabba",
        "a" * 1000 + "b" + "a" * 1000,
        "Aa",
    ]

    for test in test_inputs:
        result = longest_palindromic_substring(test)
        print(f"Input: {test!r}")
        print(f"Longest Palindromic Substring: {result!r}\n")
```