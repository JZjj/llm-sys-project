```python
import string

def main():
    paragraph = input("Enter a paragraph of text:\n")

    # Normalize case and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    paragraph = paragraph.lower().translate(translator)

    # Split into words and count frequencies
    freq = {}
    for word in paragraph.split():
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency descending, then alphabetically ascending
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Print results
    for word, count in sorted_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
```