```python
#!/usr/bin/env python3
"""
A Python program to group anagrams from a list of strings.
"""

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings into anagram groups.

    Parameters:
        strs (List[str]): List of input strings.

    Returns:
        List[List[str]]: List of groups, each group is a list of anagram strings.
    """
    anagram_map = defaultdict(list)
    for s in strs:
        # Normalize to lowercase to handle mixed case letters
        normalized = s.lower()
        # Use a tuple of sorted characters as key for grouping anagrams
        key = tuple(sorted(normalized))
        anagram_map[key].append(s)
    return list(anagram_map.values())


def _test():
    # Test cases including empty strings and mixed case letters
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["", "b", "B"], [[""], ["b", "B"]]),
        (["abc", "CAB", "bCa"], [["abc", "CAB", "bCa"]]),
        ([], []),
        (["Listen", "Silent", "enlist", "in lets"], [["Listen", "Silent", "enlist"], ["in lets"]]),
    ]

    for i, (input_list, expected_groups) in enumerate(test_cases, 1):
        result = group_anagrams(input_list)
        # For testing, convert lists of groups to sets of frozensets for order-insensitive comparison
        result_set = {frozenset(group) for group in result}
        expected_set = {frozenset(group) for group in expected_groups}
        assert result_set == expected_set, f"Test case {i} failed"
    print("All test cases passed.")


if __name__ == "__main__":
    _test()
```