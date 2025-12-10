```python
import string

def count_unique_words(text: str) -> int:
    """
    Count the number of unique words in the given text, ignoring case and punctuation.

    Parameters:
        text (str): The input string to analyze.

    Returns:
        int: The count of unique words in the text. Returns 0 if the input is empty or contains no words.
    """
    if not text:
        return 0

    # Normalize text to lowercase
    normalized_text = text.lower()

    # Remove punctuation using str.translate and string.punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = normalized_text.translate(translator)

    # Split the cleaned text into words based on whitespace
    words = cleaned_text.split()

    # Use a set to find unique words
    unique_words = set(words)

    return len(unique_words)


if __name__ == "__main__":
    # Example usage and simple test cases
    test_cases = [
        ("Hello, hello! World.", 2),
        ("", 0),
        ("Python python Python.", 1),
        ("This is a test. This test is simple!", 5),
        ("Punctuation: should; not, affect! count?", 5),
        ("Mixed CASE words mixed CASE Words.", 3),
        ("One-word", 1),
        ("Multiple     spaces\tand\nnewlines.", 4),
    ]

    for i, (input_text, expected_count) in enumerate(test_cases, 1):
        result = count_unique_words(input_text)
        print(f"Test case {i}: Input: {input_text!r}")
        print(f"Expected unique words: {expected_count}, Got: {result}")
        assert result == expected_count, f"Test case {i} failed"
    print("All tests passed.")
```