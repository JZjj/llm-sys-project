```python
from collections import defaultdict

def find_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagram_groups[key].append(word)

    result_set = {word for group in anagram_groups.values() if len(group) > 1 for word in group}

    return sorted(result_set)


if __name__ == "__main__":
    sample = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
    print(find_anagrams(sample))
```