from typing import List, Dict, Tuple

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map: Dict[Tuple[str, ...], List[str]] = {}

    for word in words:
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)  # Output order may vary but groups are correct