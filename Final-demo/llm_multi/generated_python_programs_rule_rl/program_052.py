from collections import Counter

def can_form_palindrome_anagram(s: str) -> bool:
    """
    Check if any anagram of the input string can form a palindrome.

    Args:
        s (str): Input string.

    Returns:
        bool: True if a palindrome anagram exists, False otherwise.
    """
    # Filter only alphabetic characters and convert to lowercase
    filtered_chars = [ch.lower() for ch in s if ch.isalpha()]

    # Count frequency of each character
    char_counts = Counter(filtered_chars)

    # Count how many characters have an odd count
    odd_count_chars = sum(1 for count in char_counts.values() if count % 2 != 0)

    # For palindrome formation:
    # If length is even, no odd counts allowed.
    # If length is odd, only one odd count allowed.
    # Empty string is considered palindrome.
    return odd_count_chars <= 1

if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ("Tact Coa", True),
        ("Hello", False),
        ("", True),
        ("A man a plan a canal Panama", True),
        ("No lemon, no melon", True),
        ("abc", False),
        ("aaabbbb", True),
        ("racecar", True),
        ("123@!aA", True),  # Only 'a' counts, so palindrome possible
    ]

    for input_str, expected in test_cases:
        result = can_form_palindrome_anagram(input_str)
        print(f"Input: {input_str!r} -> Can form palindrome anagram? {result} (Expected: {expected})")