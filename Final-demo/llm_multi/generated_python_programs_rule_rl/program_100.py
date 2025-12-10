from typing import List, Dict

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups a list of lowercase strings into lists of anagrams.

    Args:
        words (List[str]): List of lowercase strings.

    Returns:
        List[List[str]]: List of groups, each containing anagrams.
    """
    anagram_map: Dict[str, List[str]] = {}

    for word in words:
        # Sort the word to get the key representing its anagram group
        sorted_word = ''.join(sorted(word))
        anagram_map.setdefault(sorted_word, []).append(word)

    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())


if __name__ == "__main__":
    # Example usage and simple test cases
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    result = group_anagrams(test_input)

    # Since the order does not matter, convert to sets of frozensets for comparison
    result_sets = {frozenset(group) for group in result}
    expected_sets = {frozenset(group) for group in expected_output}

    print("Input:", test_input)
    print("Grouped Anagrams:", result)
    print("Test passed:", result_sets == expected_sets)