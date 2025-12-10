```python
def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    start, max_len = 0, 1

    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(n):
        l1, r1 = expand_around_center(i, i)
        length1 = r1 - l1 + 1
        if length1 > max_len:
            max_len = length1
            start = l1

        l2, r2 = expand_around_center(i, i + 1)
        length2 = r2 - l2 + 1
        if length2 > max_len:
            max_len = length2
            start = l2

    return s[start:start + max_len]


if __name__ == "__main__":
    input_str = input().rstrip('\n')
    print(longest_palindromic_substring(input_str))
```