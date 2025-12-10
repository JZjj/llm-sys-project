```python
from collections import defaultdict
from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase words into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of lists where each sublist contains anagrams.
    """
    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    sample_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(sample_input))
```