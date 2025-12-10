from typing import List, Dict


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Find groups of anagrams in the given list of words.
    Each group contains words that are anagrams of each other.
    Groups and words within each group are sorted alphabetically.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Key by sorted characters of the word
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    groups = [sorted(group_words) for group_words in anagram_map.values()]
    groups.sort(key=lambda grp: grp[0])
    return groups


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "rat", "tar", "art"]
    result = find_anagram_groups(input_words)
    for group in result:
        print(group)