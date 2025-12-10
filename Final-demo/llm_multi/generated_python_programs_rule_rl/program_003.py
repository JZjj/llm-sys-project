def find_anagrams(strings):
    """
    Returns a list of strings that have at least one anagram counterpart in the input list.
    The order of strings in the output list is the same as their first occurrence in the input.
    """
    from collections import defaultdict

    anagram_groups = defaultdict(list)
    for s in strings:
        key = tuple(sorted(s))
        anagram_groups[key].append(s)

    result = []
    seen = set()
    for s in strings:
        key = tuple(sorted(s))
        if len(anagram_groups[key]) > 1 and s not in seen:
            result.append(s)
            seen.add(s)

    return result


if __name__ == "__main__":
    input_list = ["listen", "silent", "enlist", "google", "gooegl", "abc"]
    output_list = find_anagrams(input_list)
    print(output_list)  # Expected: ["listen", "silent", "enlist", "google", "gooegl"]