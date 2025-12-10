from typing import List, Dict


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase alphabetic strings.

    Returns:
        List[List[str]]: A list where each sublist contains words that are anagrams of each other.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Sort the word to create a key that will be the same for all anagrams
        sorted_word = ''.join(sorted(word))
        anagram_map.setdefault(sorted_word, []).append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test
    input_words = ["listen", "silent", "enlist", "hello", "ohlle", "world"]
    grouped = group_anagrams(input_words)
    for group in grouped:
        print(group)