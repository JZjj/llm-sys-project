from typing import List
from collections import defaultdict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.
    Each sublist and the list of sublists are sorted alphabetically.

    :param words: List of lowercase strings.
    :return: List of lists of anagrams sorted alphabetically.
    """
    anagram_map = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    grouped_anagrams = [sorted(group) for group in anagram_map.values()]
    grouped_anagrams.sort(key=lambda x: x[0] if x else "")

    return grouped_anagrams


if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    result = group_anagrams(input_words)
    print(result)  # Expected: [['abc', 'cab'], ['enlist', 'listen', 'silent'], ['google', 'gooegl']]