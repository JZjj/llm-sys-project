from typing import List, Dict
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        strs (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map: Dict[str, List[str]] = defaultdict(list)

    for s in strs:
        # Sort the string to get the key representing its anagram group
        key = ''.join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_strings)
    print(grouped)  # Output can be in any order, e.g. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]