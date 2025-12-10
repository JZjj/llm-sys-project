from typing import List, Dict, Tuple

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase alphabetic strings into anagrams.
    Returns a list of groups sorted by frequency descending,
    and alphabetically by the first word if frequencies are equal.
    Each group is sorted alphabetically.
    """
    anagram_map: Dict[Tuple[str, ...], List[str]] = {}

    for word in words:
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    groups = [sorted(group) for group in anagram_map.values()]
    groups.sort(key=lambda g: (-len(g), g[0]))

    return groups


if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_words)
    print(result)  # Expected: [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]