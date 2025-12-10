```python
from collections import defaultdict
from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups words that are anagrams of each other.

    Args:
        words (List[str]): List of words to group.

    Returns:
        List[List[str]]: List of groups of anagrams.
    """
    anagram_map = defaultdict(list)
    for word in words:
        # Sort the word to get the key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "hello", "ohlle"]
    grouped = group_anagrams(input_words)
    print(grouped)
```