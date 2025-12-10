```python
def find_longest_common_substring(words):
    substring_map = {}

    for word in words:
        length = len(word)
        seen_substrings = set()
        for start in range(length):
            for end in range(start + 1, length + 1):
                sub = word[start:end]
                if sub not in seen_substrings:
                    seen_substrings.add(sub)
                    substring_map.setdefault(sub, set()).add(word)

    longest_substring = ""
    for sub, word_set in substring_map.items():
        if len(word_set) >= 2 and len(sub) > len(longest_substring):
            longest_substring = sub

    if not longest_substring:
        return None, []
    return longest_substring, sorted(substring_map[longest_substring])


def main():
    words = input().strip().split()
    substring, word_list = find_longest_common_substring(words)

    if substring is None:
        print("No common substring found.")
    else:
        print(f'Longest common substring: "{substring}"')
        print(f"Words containing substring: {word_list}")


if __name__ == "__main__":
    main()
```