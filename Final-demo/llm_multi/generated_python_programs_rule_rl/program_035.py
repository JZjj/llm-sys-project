from typing import List, Dict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.
    Each group is sorted alphabetically.
    The list of groups is sorted by the first element of each group.

    :param strs: List of lowercase strings
    :return: List of lists of anagrams
    """
    anagram_map: Dict[str, List[str]] = {}

    for s in strs:
        # Sort the string to get the anagram key
        key = ''.join(sorted(s))
        anagram_map.setdefault(key, []).append(s)

    # Sort each group alphabetically
    groups = [sorted(group) for group in anagram_map.values()]

    # Sort groups by the first element of each group
    groups.sort(key=lambda x: x[0])

    return groups


if __name__ == "__main__":
    # Example usage
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_strings)
    print(grouped)  # Expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]