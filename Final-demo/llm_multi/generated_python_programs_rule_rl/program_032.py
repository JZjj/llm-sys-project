from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings into anagrams.
    
    Args:
        strs: List of lowercase alphabet strings.
    
    Returns:
        A list of groups of anagrams, each group sorted alphabetically,
        and groups sorted by their first member alphabetically.
    """
    if not strs:
        return []

    anagram_map = {}
    for s in strs:
        key = tuple(sorted(s))
        anagram_map.setdefault(key, []).append(s)

    groups = [sorted(group) for group in anagram_map.values()]
    groups.sort(key=lambda x: x[0])

    return groups

if __name__ == "__main__":
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_list)
    print(result)  # Expected output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]