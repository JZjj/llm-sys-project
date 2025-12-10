from typing import List
from collections import defaultdict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups anagrams together from the input list of words.
    Anagrams are identified case-insensitively but original casing is preserved.
    Each group is sorted alphabetically, and groups are sorted by their first word.
    """
    anagram_map = defaultdict(list)

    for word in words:
        key = tuple(sorted(word.lower()))
        anagram_map[key].append(word)

    grouped_anagrams = [sorted(group) for group in anagram_map.values()]
    grouped_anagrams.sort(key=lambda group: group[0].lower())

    return grouped_anagrams


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
    result = group_anagrams(input_words)
    print(result)  # Expected: [['abc'], ['enlist', 'listen', 'silent'], ['google', 'gooegl']]