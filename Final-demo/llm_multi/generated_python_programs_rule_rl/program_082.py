from typing import List, Dict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.
    Each group is sorted alphabetically.
    The list of groups is sorted by the first element of each group.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    grouped_anagrams = [sorted(group) for group in anagram_map.values()]
    grouped_anagrams.sort(key=lambda group: group[0])

    return grouped_anagrams


if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_words)
    print(result)  # Expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]