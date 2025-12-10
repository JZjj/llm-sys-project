import sys
import string
from collections import Counter

def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.
    """
    return word == word[::-1]

def extract_words(text: str) -> list:
    """
    Extract words from text, considering only alphabetic characters and ignoring case.
    """
    # Translate punctuation to spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(translator)
    # Split and filter alphabetic words
    words = [word.lower() for word in cleaned_text.split() if word.isalpha()]
    return words

def top_palindromic_words(file_path: str, top_n: int = 5) -> list:
    """
    Read the file and return the top N most frequent palindromic words with their counts.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        return []

    words = extract_words(text)
    palindromic_words = [word for word in words if is_palindrome(word)]

    if not palindromic_words:
        return []

    counter = Counter(palindromic_words)
    top_palindromes = counter.most_common(top_n)
    return top_palindromes

def main():
    """
    Example usage of the program.
    """
    if len(sys.argv) != 2:
        print("Usage: python palindromic_words.py <text_file_path>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    result = top_palindromic_words(file_path)

    if not result:
        print("No palindromic words found.")
        sys.exit(0)

    print("Top palindromic words and their counts:")
    for word, count in result:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()