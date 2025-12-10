from typing import List
from collections import defaultdict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase alphabetic strings into lists of anagrams.
    Each group is sorted lexicographically, and the list of groups is sorted
    by the first word in each group.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups of anagrams.
    """
    # Filter to keep only lowercase alphabetic words
    filtered_words = [word for word in words if word.isalpha() and word.islower()]

    anagram_map = defaultdict(list)

    # Group words by their sorted character tuple
    for word in filtered_words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    # Sort each group lexicographically
    groups = [sorted(group) for group in anagram_map.values()]

    # Sort groups by the first word in each group
    groups.sort(key=lambda g: g[0])

    return groups


if __name__ == "__main__":
    # Example usage and simple test
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_words)
    print(result)
    # Expected output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]