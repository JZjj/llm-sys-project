from typing import List, Dict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words: List of lowercase strings.

    Returns:
        A list of lists, where each sublist contains strings that are anagrams of each other.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Sort the characters in the word to form the key
        key = ''.join(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test
    input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_words)
    print(grouped)  # Output can be in any order, e.g. [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]