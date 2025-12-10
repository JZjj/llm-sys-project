from typing import List, Dict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.
    Each sublist is sorted lexicographically.
    The overall list is sorted by the first element of each sublist.

    :param strs: List of lowercase strings
    :return: List of lists of grouped anagrams
    """
    anagram_map: Dict[str, List[str]] = {}

    # Group strings by their sorted character string as the key
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map.setdefault(key, []).append(s)

    # Sort each group lexicographically
    grouped = [sorted(group) for group in anagram_map.values()]

    # Sort groups by their first element
    grouped.sort(key=lambda x: x[0])

    return grouped


if __name__ == "__main__":
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_strings)
    print(result)  # Expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]