```python
from collections import defaultdict
from typing import List

def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Groups words that are anagrams of each other.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of lists, each containing anagram words.
    """
    anagram_map = defaultdict(list)
    for word in words:
        # Use sorted tuple of characters as the key
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    # Example usage
    example_words = ["listen", "silent", "enlist", "hello", "ohlle"]
    groups = find_anagram_groups(example_words)
    print(groups)
```