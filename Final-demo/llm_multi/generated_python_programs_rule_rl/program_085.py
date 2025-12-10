def longest_k_distinct(s: str, k: int) -> str:
    """
    Returns the longest substring of s that contains exactly k distinct characters.
    If multiple substrings have the same maximum length, returns the first one.
    If no such substring exists, returns an empty string.
    """
    if k <= 0 or not s:
        return ""

    n = len(s)
    char_count = {}
    left = 0
    max_len = 0
    max_start = 0

    for right in range(n):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        if len(char_count) == k:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                max_start = left

    return s[max_start:max_start + max_len] if max_len > 0 else ""


if __name__ == "__main__":
    # Sample test cases to verify the function behavior
    test_cases = [
        ("araaci", 2, "araa"),
        ("araaci", 1, "aa"),
        ("cbbebi", 3, "cbbeb"),
        ("abc", 4, ""),
        ("aabbcc", 1, "aa"),
        ("aabbcc", 2, "aabb"),
        ("aabbcc", 3, "aabbcc"),
        ("", 1, ""),
        ("abc", 0, ""),
        ("abc", -1, ""),
    ]

    for s, k, expected in test_cases:
        result = longest_k_distinct(s, k)
        print(f"longest_k_distinct({s!r}, {k}) = {result!r} (expected: {expected!r})")