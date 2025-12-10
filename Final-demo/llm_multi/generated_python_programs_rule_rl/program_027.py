import re

def evaluate_expressions(expressions):
    """
    Evaluate a list of mathematical expressions safely without using eval().
    Supports non-negative integers and operators +, -, *, / with correct precedence.
    Returns a list of floats or None for invalid expressions or division by zero.
    """
    def tokenize(expr):
        # Tokenize the expression into numbers and operators
        token_pattern = re.compile(r'\s*(\d+|[+\-*/])\s*')
        tokens = token_pattern.findall(expr)
        # Check if the entire expression was tokenized
        joined_tokens = ''.join(tokens)
        expr_no_space = re.sub(r'\s+', '', expr)
        if joined_tokens != expr_no_space:
            # Contains invalid characters or unsupported parentheses
            return None
        return tokens

    def shunting_yard(tokens):
        # Convert infix tokens to Reverse Polish Notation using the Shunting Yard algorithm
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.isdigit():
                output_queue.append(token)
            elif token in precedence:
                while (operator_stack and operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                # Invalid token
                return None

        while operator_stack:
            if operator_stack[-1] not in precedence:
                return None
            output_queue.append(operator_stack.pop())

        return output_queue

    def evaluate_rpn(rpn_tokens):
        # Evaluate the expression in Reverse Polish Notation
        stack = []
        for token in rpn_tokens:
            if token.isdigit():
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    return None
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        return None
                    stack.append(a / b)
                else:
                    return None
        if len(stack) != 1:
            return None
        return stack[0]

    results = []
    for expr in expressions:
        tokens = tokenize(expr)
        if tokens is None:
            results.append(None)
            continue
        rpn = shunting_yard(tokens)
        if rpn is None:
            results.append(None)
            continue
        value = evaluate_rpn(rpn)
        results.append(value)
    return results


if __name__ == "__main__":
    # Example usage and simple test cases
    test_expressions = [
        "3 + 5 * 2",
        "10 / 2 - 3",
        "8 + 2 * 5 / (1 + 1)",  # Contains parentheses, should be invalid -> None
        "7 + 3 / 0",            # Division by zero -> None
        "4 + 5 *",              # Invalid expression -> None
        "  12  *  3 - 4 / 2 ",  # Valid expression with whitespace
        "100 / 25 + 6 - 2 * 3"
    ]
    results = evaluate_expressions(test_expressions)
    for expr, result in zip(test_expressions, results):
        print(f"Expression: {expr} => Result: {result}")