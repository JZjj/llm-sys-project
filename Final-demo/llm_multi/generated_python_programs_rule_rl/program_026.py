from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups of anagrams, each sorted alphabetically,
                         and the groups sorted by their first element.
    """
    anagram_map: Dict[str, List[str]] = {}

    # Group words by their sorted character string as the key
    for word in words:
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    # Sort each group alphabetically
    grouped_anagrams = [sorted(group) for group in anagram_map.values()]

    # Sort groups by the first element of each group
    grouped_anagrams.sort(key=lambda group: group[0])

    return grouped_anagrams


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    result = group_anagrams(input_words)
    print(result)
    # Expected output:
    # [["abc", "cab"], ["enlist", "listen", "silent"], ["google", "gooegl"]]