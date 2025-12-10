```python
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        strs (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map = defaultdict(list)
    for s in strs:
        # Using sorted tuple of characters as key for anagrams
        key = tuple(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_data)
    print(grouped)
```