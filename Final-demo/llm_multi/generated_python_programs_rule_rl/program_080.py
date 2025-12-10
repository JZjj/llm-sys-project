import re

def validate_and_reformat_phone_numbers(phone_numbers):
    """
    Validate and reformat phone numbers to E.164 format.

    Args:
        phone_numbers (list of str): List of phone number strings.

    Returns:
        list of str: Valid phone numbers formatted in E.164.
    """
    e164_numbers = []

    # Allowed characters: digits, space, dash, parentheses, plus sign only at start
    allowed_pattern = re.compile(r'^\+?[\d\s\-\(\)]*$')

    for number in phone_numbers:
        if not isinstance(number, str):
            # Skip non-string entries
            continue

        number = number.strip()
        if not number:
            continue

        # Validate allowed characters with plus sign only at start
        if not allowed_pattern.match(number):
            continue

        # Remove all non-digit characters except leading +
        if number.startswith('+'):
            # Remove all non-digits after plus
            digits = '+' + re.sub(r'\D', '', number[1:])
        else:
            digits = re.sub(r'\D', '', number)

        if digits.startswith('+'):
            # Validate digits after '+'
            if len(digits) <= 1 or not digits[1:].isdigit():
                continue
            # E.164 numbers must be between 8 and 15 digits (excluding '+')
            if len(digits[1:]) < 8 or len(digits[1:]) > 15:
                continue
            e164_numbers.append(digits)
        else:
            # Only digits, prepend default country code +1
            if not digits.isdigit() or len(digits) == 0:
                continue
            digits_stripped = digits.lstrip('0')
            if not digits_stripped:
                # All zeros, invalid
                continue
            # US numbers typically 10 digits, allow 7-11 digits for leniency
            if len(digits_stripped) < 7 or len(digits_stripped) > 11:
                continue
            e164_numbers.append('+1' + digits_stripped)

    return e164_numbers


if __name__ == "__main__":
    # Example inputs with various formats
    sample_numbers = [
        "202-555-0173",
        "(202) 555 0173",
        "+44 20 7946 0958",
        "001-541-754-3010",
        "+49-89-636-48018",
        "5550123",
        "1234567890",
        "+81(3)1234-5678",
        "++12345678",
        "abc-123-4567",
        "123 456 7890 ext. 123",
        "+1 (800) 555-0199",
        "000-000-0000",
        " +49 (0) 30 123456 ",
        "++1 234 567 890",
        "",
        None,
        1234567890,
    ]

    reformatted = validate_and_reformat_phone_numbers(sample_numbers)
    for num in reformatted:
        print(num)