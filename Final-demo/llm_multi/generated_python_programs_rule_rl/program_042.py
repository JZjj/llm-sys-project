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
        # Sort the word to get the key representing its anagram group
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple tests
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)  # Output order may vary but groups should be correct

    empty_test = group_anagrams([])
    print(empty_test)  # Should print []