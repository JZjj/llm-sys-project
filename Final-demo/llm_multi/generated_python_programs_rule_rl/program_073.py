import re

def evaluate_expressions(expressions):
    """
    Safely parse and evaluate a list of mathematical expressions containing only integers,
    addition (+), and multiplication (*). Invalid expressions are skipped.

    Args:
        expressions (list of str): List of expression strings.

    Returns:
        list of int: Evaluated results of valid expressions.
    """

    def tokenize(expr):
        """
        Tokenize the expression into integers and operators.
        Returns a list of tokens or None if invalid characters are found.
        """
        # Allowed tokens: integers, +, *
        token_pattern = re.compile(r'\d+|[+*]')
        tokens = token_pattern.findall(expr)
        # Check if the entire expression is covered by tokens (no invalid chars)
        combined = ''.join(tokens)
        if combined.replace(' ', '') != expr.replace(' ', ''):
            return None
        return tokens

    def parse_and_eval(tokens):
        """
        Parse tokens and evaluate the expression respecting operator precedence:
        multiplication before addition.
        Returns the integer result or None if invalid syntax.
        """

        if not tokens:
            return None

        # Basic validation: expression cannot start or end with operator
        if tokens[0] in '+*' or tokens[-1] in '+*':
            return None

        # Validate token sequence: must alternate between number and operator
        # Even indices: numbers, Odd indices: operators
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                # Should be integer
                if not token.isdigit():
                    return None
            else:
                # Should be operator + or *
                if token not in ('+', '*'):
                    return None

        # First pass: handle multiplication
        new_tokens = []
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit():
                current_value = int(tokens[i])
                i += 1
                while i < len(tokens) and tokens[i] == '*':
                    i += 1
                    if i >= len(tokens) or not tokens[i].isdigit():
                        return None
                    current_value *= int(tokens[i])
                    i += 1
                new_tokens.append(str(current_value))
            else:
                return None

            if i < len(tokens) and tokens[i] == '+':
                new_tokens.append('+')
                i += 1

        # Second pass: handle addition
        result = 0
        i = 0
        while i < len(new_tokens):
            if new_tokens[i].isdigit():
                result += int(new_tokens[i])
                i += 1
            elif new_tokens[i] == '+':
                i += 1
            else:
                return None

        return result

    results = []
    for expr in expressions:
        expr_stripped = expr.strip()
        if not expr_stripped:
            continue
        tokens = tokenize(expr_stripped)
        if tokens is None:
            continue
        value = parse_and_eval(tokens)
        if value is not None:
            results.append(value)
    return results


if __name__ == "__main__":
    # Example usage and simple tests
    test_expressions = [
        "2 + 3 * 4",    # 2 + 12 = 14
        "10 + 5 + 2",   # 17
        "3 * 3 * 3",    # 27
        "4 + 5 *",      # invalid
        "7 + a + 2",    # invalid
        "  8*  2 + 1 ", # 17
        "",             # skip
        "42",           # 42
        "1 + 2 * 3 + 4 * 5", # 1 + 6 + 20 = 27
    ]

    results = evaluate_expressions(test_expressions)
    for expr, res in zip(test_expressions, results):
        print(f"Expression: {expr!r} => Result: {res}")