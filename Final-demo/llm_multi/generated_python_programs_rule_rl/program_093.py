from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        strs: List of lowercase strings.

    Returns:
        A list of lists, where each inner list contains strings that are anagrams of each other.
    """
    anagram_map = defaultdict(list)
    for s in strs:
        # Use the sorted tuple of characters as the key
        key = tuple(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_strings)
    print(grouped)  # Output can be in any order, e.g. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]