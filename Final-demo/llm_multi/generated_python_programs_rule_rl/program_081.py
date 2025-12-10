import re

def validate_and_format_phone_numbers(phone_numbers):
    """
    Validate and reformat a list of international phone numbers.

    Args:
        phone_numbers (list of str): List of phone number strings.

    Returns:
        list of str: List of reformatted valid phone numbers.
    """
    reformatted_numbers = []
    pattern = re.compile(r'^\+(\d{8,15})$')  # Matches '+' followed by 8 to 15 digits only

    for number in phone_numbers:
        match = pattern.fullmatch(number)
        if not match:
            # Invalid number, skip
            continue

        digits = match.group(1)

        groups = []
        i = 0
        length = len(digits)

        # Group digits into blocks of three from left to right,
        # the last group may have fewer than three digits.
        while i < length:
            group_size = 3 if length - i > 3 else length - i
            groups.append(digits[i:i+group_size])
            i += group_size

        reformatted = '+' + ' '.join(groups)
        reformatted_numbers.append(reformatted)

    return reformatted_numbers


if __name__ == "__main__":
    input_numbers = ['+1234567890', '123456', '+987654321012345', '+12abc345678']
    output = validate_and_format_phone_numbers(input_numbers)
    print(output)  # Expected: ['+123 456 789 0', '+987 654 321 012 345']