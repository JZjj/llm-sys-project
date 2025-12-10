```python
from typing import List
from collections import defaultdict


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Find groups of anagrams in the input list of words.

    Args:
        words: List of words (strings).

    Returns:
        A list of groups (list of strings), where each group contains at least two
        words that are anagrams of each other.
        Groups and words within each group are sorted alphabetically (case-sensitive),
        but grouping is done case-insensitively.
    """
    anagram_map = defaultdict(list)

    for word in words:
        # Normalize word to lowercase and sort letters for the key
        key = ''.join(sorted(word.lower()))
        anagram_map[key].append(word)

    # Filter groups with at least two words and sort each group alphabetically
    filtered_groups = [
        sorted(group)
        for group in anagram_map.values()
        if len(group) > 1
    ]

    # Sort groups alphabetically by their first member
    filtered_groups.sort(key=lambda group: group[0])

    return filtered_groups
```