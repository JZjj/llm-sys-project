```python
def group_anagrams(words):
    """
    Groups a list of lowercase strings into lists of anagrams.

    Parameters:
    words (list of str): List of lowercase words.

    Returns:
    list of list of str: Groups of anagrams.
    """
    anagram_map = {}
    for word in words:
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage
    sample_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(sample_words)
    print(grouped)
```