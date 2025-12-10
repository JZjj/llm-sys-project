```python
import re
from collections import Counter

def main():
    text = input("Enter a paragraph of text:\n")
    # Extract words: sequences of alphabetic characters only, ignore case
    words = re.findall(r'[a-zA-Z]+', text.lower())
    
    counts = Counter(words)
    # Sort by frequency descending, then alphabetically ascending
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    top_n = min(3, len(sorted_words))
    for word, freq in sorted_words[:top_n]:
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
```