```python
#!/usr/bin/env python3
"""
Balanced Parentheses Validator

This program defines a function to check if a given string has balanced parentheses.
It considers three types of parentheses: round (), square [], and curly {}.
Non-parentheses characters are ignored.

Author: Senior Python Engineer
Date: 2024-06
"""

def is_balanced_parentheses(s: str) -> bool:
    """
    Check if the input string has balanced parentheses.

    Args:
        s (str): The input string potentially containing parentheses.

    Returns:
        bool: True if balanced, False otherwise.
    """
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    # Stack to keep track of opening brackets encountered
    stack = []

    for char in s:
        # If it's an opening bracket, push onto the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If it's a closing bracket, check stack top for match
        elif char in bracket_pairs:
            # If stack empty or top doesn't match the expected opening bracket, unbalanced
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
        # Ignore all other characters

    # If stack empty at the end, all brackets matched correctly
    return not stack


def main():
    """
    Main function to interactively test the balanced parentheses validator.
    """
    print("Balanced Parentheses Validator")
    print("Enter strings to check for balanced parentheses.")
    print("Type 'exit' or press Ctrl+C to quit.")

    try:
        while True:
            user_input = input("> ")
            if user_input.strip().lower() == 'exit':
                print("Exiting.")
                break
            result = is_balanced_parentheses(user_input)
            print("Balanced" if result else "Not Balanced")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
```