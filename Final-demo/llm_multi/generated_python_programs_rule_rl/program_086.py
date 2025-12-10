from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of anagram groups sorted as specified.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Use tuple of sorted characters as key for better hashing performance
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    groups = [sorted(group) for group in anagram_map.values()]
    groups.sort(key=lambda g: (-len(g), g[0]))

    return groups


if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = group_anagrams(input_words)
    print(output)
    # Expected output:
    # [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]