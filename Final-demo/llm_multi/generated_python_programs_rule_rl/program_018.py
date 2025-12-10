def evaluate_expression(expression: str) -> int:
    """
    Evaluate a mathematical expression string containing non-negative integers and operators +, -, *, /.
    Operator precedence is respected: * and / before + and -.
    Division is integer division.
    Assumes the input expression is valid and does not contain division by zero.
    """
    numbers = []
    operators = []

    i = 0
    length = len(expression)
    prev_op = '+'  # To handle the first number correctly

    while i < length:
        char = expression[i]
        if char.isdigit():
            start = i
            while i < length and expression[i].isdigit():
                i += 1
            current_number = int(expression[start:i])

            if prev_op == '*':
                numbers[-1] = numbers[-1] * current_number
            elif prev_op == '/':
                numbers[-1] = numbers[-1] // current_number
            else:
                numbers.append(current_number)
        else:
            # char is an operator
            if char in '+-':
                operators.append(char)
                prev_op = char
            elif char in '*/':
                prev_op = char
            i += 1

    result = numbers[0]
    for idx, op in enumerate(operators):
        if op == '+':
            result += numbers[idx + 1]
        else:  # op == '-'
            result -= numbers[idx + 1]

    return result


if __name__ == "__main__":
    test_expression = "3+5*2-8/4"
    print(evaluate_expression(test_expression))  # Expected output: 10