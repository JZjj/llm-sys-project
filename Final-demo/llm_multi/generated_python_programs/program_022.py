```python
from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups words that are anagrams of each other.

    Args:
        words (List[str]): List of input words.

    Returns:
        List[List[str]]: List of groups of anagrams.
    """
    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())


def main():
    words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]
    grouped = group_anagrams(words)
    for group in grouped:
        print(group)


if __name__ == "__main__":
    main()
```