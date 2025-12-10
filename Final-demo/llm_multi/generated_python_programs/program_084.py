```python
from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]
    grouped = group_anagrams(input_words)
    print(grouped)
```