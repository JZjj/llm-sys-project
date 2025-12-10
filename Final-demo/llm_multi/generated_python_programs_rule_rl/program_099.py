from collections import defaultdict
from typing import List

def group_anagrams_by_frequency(words: List[str]) -> List[List[str]]:
    """
    Groups words that are anagrams and sorts the groups by the total frequency
    of their characters across all words in the group, in descending order.
    Each group is sorted lexicographically.
    """
    anagram_groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagram_groups[key].append(word)

    groups_with_counts = []
    for group_words in anagram_groups.values():
        sorted_group = sorted(group_words)
        total_char_count = sum(len(word) for word in sorted_group)
        groups_with_counts.append((total_char_count, sorted_group))

    groups_with_counts.sort(key=lambda x: x[0], reverse=True)

    return [group for _, group in groups_with_counts]

if __name__ == "__main__":
    input_words = ["listen", "silent", "enlist", "google", "gooegl", "abc", "cab"]
    result = group_anagrams_by_frequency(input_words)
    print(result)