def count_anagram_counts(strings):
    """
    Given a list of strings, return a dictionary where each key is a string from the list,
    and the value is the count of how many other strings in the list are anagrams of the key.
    Comparison is case-insensitive and ignores spaces.
    """
    # Normalize strings: lowercase and remove spaces
    normalized_map = {}
    for s in strings:
        normalized = ''.join(sorted(s.replace(' ', '').lower()))
        normalized_map.setdefault(normalized, []).append(s)

    # Build result dictionary
    result = {}
    for s in strings:
        normalized = ''.join(sorted(s.replace(' ', '').lower()))
        # Count of anagrams excluding the string itself
        count = len(normalized_map[normalized]) - 1
        result[s] = count

    return result


if __name__ == "__main__":
    # Example usage
    input_list = ["listen", "silent", "enlist", "google", "goo gel"]
    output = count_anagram_counts(input_list)
    print(output)