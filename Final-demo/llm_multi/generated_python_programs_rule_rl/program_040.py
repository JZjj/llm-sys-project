from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups words that are anagrams of each other.
    Each group is sorted alphabetically.
    The list of groups is sorted by the first word in each group.

    :param words: List of input words
    :return: List of lists of anagram groups
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Use the sorted string of characters as the key
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    # Sort each group alphabetically
    grouped_anagrams = [sorted(group) for group in anagram_map.values()]

    # Sort groups by the first word in each group
    grouped_anagrams.sort(key=lambda group: group[0])

    return grouped_anagrams


if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "rat", "tar"]
    result = group_anagrams(input_words)
    for group in result:
        print(group)