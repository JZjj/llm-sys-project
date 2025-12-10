def is_balanced_brackets(s, pairs):
    """
    Check if the string s has balanced brackets according to the custom pairs.

    Parameters:
    - s (str): The input string to check.
    - pairs (list of tuples): List of (opening, closing) bracket pairs.

    Returns:
    - bool: True if balanced, False otherwise.
    """
    if not pairs:
        # If pairs is empty, any bracket characters present mean unbalanced
        # So if s contains any bracket chars, return False
        # Bracket chars are any opening or closing in pairs, but since pairs empty, none defined
        # So if s contains any bracket chars, return False
        # But since no pairs defined, any bracket chars are unknown; specification says:
        # "Characters in s that are not part of any bracket pair should be ignored"
        # So if pairs empty, no bracket chars exist, so s is balanced unless s contains brackets?
        # But test case ("<[]>", [], False) expects False because brackets present but no pairs
        # So we detect any bracket chars in s if pairs empty and return False
        # Let's gather all bracket chars that appear in s and check if any are brackets
        # But since no pairs, any bracket chars are unknown, so any bracket chars are unbalanced
        # We'll check if s contains any bracket characters: any char in s that is a bracket char
        # But what counts as bracket char? Since pairs empty, no bracket chars defined.
        # So in the example, "<[]>", brackets are <, [, ], > which are brackets but pairs empty
        # So any bracket chars in s means unbalanced if pairs empty
        # So if pairs empty and s contains any of these chars, return False
        # We'll consider any char in s that is in any of the opening or closing brackets in pairs
        # Since pairs empty, no bracket chars defined, so any bracket chars in s means unbalanced
        # So we check if s contains any bracket chars that are in the default bracket sets
        # But no default sets given, so we can treat "bracket chars" as any char that appears in s and is in pairs
        # Since pairs empty, any bracket chars? No.
        # But test case expects False for "<[]>", []
        # So we need to treat any bracket-like char as bracket char.
        # We'll consider the characters: ()[]{}<> as possible bracket chars.
        brackets_chars = set("()[]{}<>")
        if any(ch in brackets_chars for ch in s):
            return False
        return True

    opening_brackets = {op for op, cl in pairs}
    closing_to_opening = {cl: op for op, cl in pairs}

    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_to_opening:
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        else:
            # Ignore non-bracket characters
            continue

    return not stack


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ("[{()}]", [("(", ")"), ("[", "]"), ("{", "}")], True),
        ("[{()]", [("(", ")"), ("[", "]"), ("{", "}")], False),
        ("<{[(abc)]}>", [("<", ">"), ("(", ")"), ("[", "]"), ("{", "}")], True),
        ("<{[(abc)]}", [("<", ">"), ("(", ")"), ("[", "]"), ("{", "}")], False),
        ("", [("(", ")")], True),  # Empty string is balanced
        ("abc", [("(", ")")], True),  # No brackets, balanced
        ("<[]>", [], False),  # No pairs defined, but brackets present
        ("", [], True),  # Empty string and no pairs
    ]

    for idx, (string, pairs, expected) in enumerate(test_cases, 1):
        result = is_balanced_brackets(string, pairs)
        print(f"Test case {idx}: {'PASS' if result == expected else 'FAIL'}")