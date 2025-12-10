import sys
import string
from collections import Counter

def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome."""
    return word == word[::-1]

def clean_word(word: str) -> str:
    """Remove punctuation and convert to lowercase."""
    return word.translate(str.maketrans('', '', string.punctuation)).lower()

def get_palindromic_words(text: str) -> Counter:
    """Extract palindromic words from text and count their frequencies."""
    words = text.split()
    palindromes = []
    for word in words:
        cleaned = clean_word(word)
        if cleaned and is_palindrome(cleaned):
            palindromes.append(cleaned)
    return Counter(palindromes)

def print_top_palindromes(counter: Counter, top_n: int = 5) -> None:
    """Print the top N palindromic words with their frequencies."""
    most_common = counter.most_common(top_n)
    for word, freq in most_common:
        print(f"{word}: {freq}")

def main():
    """Main function to read file and print top palindromic words."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

    palindrome_counts = get_palindromic_words(text)

    if not palindrome_counts:
        print("No palindromic words found.")
        return

    print_top_palindromes(palindrome_counts, top_n=5)

if __name__ == "__main__":
    main()