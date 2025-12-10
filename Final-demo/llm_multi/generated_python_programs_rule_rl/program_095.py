from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase alphabetic strings into anagrams.

    :param words: List of lowercase alphabetic strings.
    :return: List of lists, where each inner list contains words that are anagrams of each other.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Sort the word to get the key representing its anagram group
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    grouped = group_anagrams(input_words)
    print(grouped)