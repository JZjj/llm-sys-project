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
    Extract alphabetic words from text, ignoring case and punctuation.
    """
    # Replace all non-alphabetic characters with spaces
    cleaned_text = ''.join(char if char.isalpha() else ' ' for char in text)
    # Split and convert to lowercase
    words = cleaned_text.lower().split()
    return words


def get_top_palindromes(words: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Get the top N most frequent palindromic words with their counts.
    """
    palindrome_counts = Counter(word for word in words if is_palindrome(word) and len(word) > 0)
    return palindrome_counts.most_common(top_n)


def read_file(filepath: str) -> str:
    """
    Read the content of a file and return it as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function demonstrating reading a file and outputting top palindrome words.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_text_file>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    text = read_file(filepath)
    words = extract_words(text)
    top_palindromes = get_top_palindromes(words, top_n=5)

    if not top_palindromes:
        print("No palindromic words found.")
    else:
        for word, count in top_palindromes:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()