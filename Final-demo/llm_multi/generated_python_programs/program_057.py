```python
from typing import List
from collections import defaultdict

def group_anagrams(words: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    print(grouped)

if __name__ == "__main__":
    main()
```