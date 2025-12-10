from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    input_words = ["bat", "tab", "eat", "tea", "tan", "nat", "ate"]
    grouped = group_anagrams(input_words)
    for group in grouped:
        print(group)