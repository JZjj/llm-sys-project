import sys
import string
from collections import Counter
from typing import List, Tuple


def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.
    """
    return word == word[::-1]


def extract_words(text: str) -> List[str]:
    """
    Extract words consisting of alphabetic characters only from the text,
    ignoring case and punctuation.
    """
    # Create a translation table that maps punctuation to None
    translator = str.maketrans('', '', string.punctuation + string.digits)
    cleaned_text = text.translate(translator)
    # Split by whitespace and filter alphabetic words
    words = [word.lower() for word in cleaned_text.split() if word.isalpha()]
    return words


def find_top_palindromic_words(words: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Find the top N most common palindromic words in a list of words.
    """
    palindromic_words = [word for word in words if is_palindrome(word)]
    counter = Counter(palindromic_words)
    return counter.most_common(top_n)


def read_file(filename: str) -> str:
    """
    Read file content safely.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to demonstrate usage.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    text = read_file(filename)
    words = extract_words(text)
    top_palindromes = find_top_palindromic_words(words, top_n=5)

    if not top_palindromes:
        print("No palindromic words found.")
        return

    print("Top 5 most common palindromic words:")
    for word, freq in top_palindromes:
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()