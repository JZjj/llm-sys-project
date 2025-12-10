```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings into anagrams.

    Args:
        strs (List[str]): List of input strings.

    Returns:
        List[List[str]]: List of groups of anagrams.
    """
    anagram_map = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())

def main():
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_list)
    print(result)

if __name__ == "__main__":
    main()
```