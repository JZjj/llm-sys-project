```python
from collections import defaultdict

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    left = 0
    max_length = 0
    char_count = defaultdict(int)

    for right, char in enumerate(s):
        char_count[char] += 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

def main():
    s = "eceba"
    k = 2
    print(length_of_longest_substring_k_distinct(s, k))  # Output: 3

if __name__ == "__main__":
    main()
```