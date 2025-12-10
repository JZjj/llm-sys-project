def longest_unique_substring(s):
    """
    Returns the longest substring without repeating characters.
    Case-sensitive: 'A' and 'a' are considered different characters.

    Args:
        s (str): Input string.

    Raises:
        TypeError: If input is not a string.

    Returns:
        str: Longest substring without repeating characters.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    start = 0  # Start index of current substring without duplicates
    max_len = 0  # Length of longest substring found
    max_start = 0  # Start index of longest substring found
    char_index_map = {}  # Map to store last index of each character

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            max_start = start

    return s[max_start:max_start + max_len]


if __name__ == "__main__":
    test_strings = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "aAbBcC",
        "",
        "abcdefg",
        "abcaefgh",
        123,
    ]

    for test_str in test_strings:
        try:
            result = longest_unique_substring(test_str)
            print(f"Input: {repr(test_str)} -> Longest substring without repeating chars: {repr(result)}")
        except TypeError as e:
            print(f"Input: {repr(test_str)} -> Error: {e}")