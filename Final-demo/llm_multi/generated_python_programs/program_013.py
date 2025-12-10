```python
import string
from collections import Counter

def main():
    filename = input("Enter the filename: ").strip()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return

    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    cleaned_text = text.translate(translator).lower()

    words = cleaned_text.split()
    if not words:
        print("No words found in the file.")
        return

    freq = Counter(words)

    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    for word, count in sorted_items[:10]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
```