def filter_palindromes(strings):
    """
    Filters the input list of strings and returns a new list containing only palindromes.
    Palindromes are checked in a case-insensitive manner and ignoring spaces.

    Args:
        strings (list of str): List of strings to filter.

    Returns:
        list of str: List containing only palindrome strings.
    
    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")

    palindromes = []
    for s in strings:
        if not isinstance(s, str):
            raise TypeError("All elements of the input list must be strings.")
        # Normalize string: remove spaces and convert to lowercase
        normalized = s.replace(" ", "").lower()
        if normalized == normalized[::-1]:
            palindromes.append(s)
    return palindromes


def main():
    # Example usage
    try:
        sample_strings = ["Race car", "hello", "madam", "Step on no pets", "world", "No lemon, no melon"]
        # Remove commas from strings for proper palindrome check (optional enhancement)
        cleaned_strings = [s.replace(",", "") for s in sample_strings]
        palindromes = filter_palindromes(cleaned_strings)
        print("Palindromes found:", palindromes)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()