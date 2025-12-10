import string

def longest_common_word_in_sentences(text):
    """
    Finds the longest word that appears in every sentence of the given text.
    Sentences are separated by periods '.'.
    Ignores punctuation other than periods and is case-insensitive.
    
    :param text: str - input string containing multiple sentences
    :return: str - the longest word appearing in every sentence or empty string if none
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Split text into sentences by period
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    if not sentences:
        return ""

    # Prepare a translation table to remove punctuation except periods
    # Actually periods are used to split sentences, so here we remove all punctuation
    # For each sentence we only want words with letters/numbers
    # We'll remove punctuation using str.translate
    remove_punct_table = str.maketrans('', '', string.punctuation.replace('.', ''))

    # Extract sets of words per sentence in lowercase, punctuation removed
    words_per_sentence = []
    for sentence in sentences:
        # Remove punctuation except periods - periods should not be present now inside sentence
        cleaned_sentence = sentence.translate(remove_punct_table)
        # Split into words, lowercase
        words = set(word.lower() for word in cleaned_sentence.split() if word)
        words_per_sentence.append(words)

    # Find intersection of all sets to get words common to every sentence
    common_words = set.intersection(*words_per_sentence)
    if not common_words:
        return ""

    # Return the longest word in common_words
    # If multiple have the same length, return the first lexicographically
    longest_word = max(common_words, key=lambda w: (len(w), -ord(w[0])))
    # Above sorting by length, tie-break by first letter (negated to keep lex order)
    # Actually better tie-break lex smallest, so:
    # Let's fix that by sorting common_words with length descending and lex ascending:
    longest_words = [w for w in common_words if len(w) == max(len(word) for word in common_words)]
    longest_word = min(longest_words)
    return longest_word


def main():
    # Example usage and simple test cases
    examples = [
        "Hello world. The world is big. In this world, we live.",
        "Python is great. I love python programming. Python, python everywhere!",
        "No common word here. Completely different sentences.",
        "Same same same. Same same same. Same same same.",
        "",
        "One sentence only no period",
        "Punctuation! should, be: ignored. Yes, ignored!"
    ]

    for i, example in enumerate(examples, 1):
        try:
            result = longest_common_word_in_sentences(example)
            print(f"Example {i}: '{example}'\nLongest common word: '{result}'\n")
        except Exception as e:
            print(f"Example {i}: Error processing input: {e}\n")


if __name__ == "__main__":
    main()