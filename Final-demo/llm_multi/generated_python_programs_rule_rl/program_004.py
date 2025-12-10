from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of strings into lists of anagrams.

    Parameters:
    words (list of str): List of lowercase alphabetic strings.

    Returns:
    list of list of str: A list where each sublist contains anagrams.
    """
    if not words:
        return []

    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)