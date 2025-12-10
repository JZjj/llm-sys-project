from typing import List
from collections import defaultdict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into anagrams.

    Args:
        words (List[str]): List of lowercase words.

    Returns:
        List[List[str]]: List of groups of anagrams, each group sorted alphabetically,
                         and the list sorted by the first word in each group.
    """
    anagram_map = defaultdict(list)

    # Group words by their sorted character tuple
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    # Sort each group alphabetically
    grouped_anagrams = [sorted(group) for group in anagram_map.values()]

    # Sort groups by the first word in each group
    grouped_anagrams.sort(key=lambda group: group[0])

    return grouped_anagrams


if __name__ == "__main__":
    # Example usage and simple test
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_words)
    print(result)  # Expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]