```python
from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        # Key is sorted lowercase characters
        key = ''.join(sorted(word.lower()))
        anagram_map[key].append(word)
    
    # Sort each group alphabetically (case-sensitive based on original words)
    groups = [sorted(group) for group in anagram_map.values()]
    
    # Sort groups by the first word in each group
    groups.sort(key=lambda g: g[0])
    return groups


def main():
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)


if __name__ == "__main__":
    main()
```