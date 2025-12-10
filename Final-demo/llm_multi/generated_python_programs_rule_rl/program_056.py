def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    char_index_map = {}
    max_length = 0
    start = 0  # Start index of current substring window

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length

    return max_length


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]

    for input_str, expected in test_cases:
        result = length_of_longest_substring(input_str)
        print(f"Input: {input_str!r} -> Output: {result} (Expected: {expected})")