from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of strings into lists of anagrams.
    Anagrams are case-insensitive but original case is preserved in output.

    :param words: List of strings to group
    :return: List of lists of anagrams
    """
    anagram_map = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        anagram_map[key].append(word)
    return list(anagram_map.values())

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]
    grouped = group_anagrams(input_words)
    print(grouped)