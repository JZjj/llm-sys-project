```python
from typing import List, Dict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams from the input list of strings.

    Args:
        strs (List[str]): List of strings to group.

    Returns:
        List[List[str]]: List of groups, each group containing anagrams.
    """
    anagram_map: Dict[str, List[str]] = {}
    for s in strs:
        # Using sorted string as the key
        key = ''.join(sorted(s))
        anagram_map.setdefault(key, []).append(s)
    return list(anagram_map.values())


def main():
    # Example usage and basic test
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(input_list)
    print(grouped)


if __name__ == "__main__":
    main()
```