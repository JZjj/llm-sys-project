```python
def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    char_index_map = {}
    max_length = 0
    start = 0  # start index of current substring without repeats

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length


def main():
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "a",
        "dvdf",
        "anviaj"
    ]

    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f'Input: "{s}" => Output: {result}')


if __name__ == "__main__":
    main()
```