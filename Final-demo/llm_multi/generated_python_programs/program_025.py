```python
from typing import List, Dict

def longest_word_chain(words: List[str]) -> List[str]:
    # Build adjacency list: for each word, list words that can follow it
    adjacency: Dict[str, List[str]] = {w: [] for w in words}
    for w1 in words:
        last_char = w1[-1]
        for w2 in words:
            if w2 != w1 and w2[0] == last_char:
                adjacency[w1].append(w2)

    max_chain: List[str] = []

    def dfs(current_word: str, visited: set, path: List[str]) -> None:
        nonlocal max_chain
        if len(path) > len(max_chain):
            max_chain = path[:]
        for next_word in adjacency[current_word]:
            if next_word not in visited:
                visited.add(next_word)
                dfs(next_word, visited, path + [next_word])
                visited.remove(next_word)

    for word in words:
        dfs(word, {word}, [word])

    return max_chain


if __name__ == "__main__":
    example_words = [
        "apple", "egg", "giraffe", "elephant", "tiger", "rhino", "octopus"
    ]
    chain = longest_word_chain(example_words)
    print("Longest word chain:")
    print(chain)
```