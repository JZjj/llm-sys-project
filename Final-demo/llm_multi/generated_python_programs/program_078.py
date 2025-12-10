```python
def group_anagrams(words):
    anagram_map = {}
    for word in words:
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)
```