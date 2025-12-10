```python
from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    
    for word in words:
        normalized = word.replace(" ", "").lower()
        key = "".join(sorted(normalized))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "goo gel", "rat", "tar"]
    grouped = group_anagrams(input_words)
    print(grouped)
```