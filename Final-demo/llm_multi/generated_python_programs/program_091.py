```python
def group_anagrams(words):
    anagram_map = {}
    for word in words:
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)
    return list(anagram_map.values())

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    print(grouped)

if __name__ == "__main__":
    main()
```