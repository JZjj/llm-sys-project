```python
import re
from typing import List

def validate_and_normalize_emails(emails: List[str]) -> List[str]:
    """
    Validate and normalize a list of email addresses.

    Args:
        emails (List[str]): List of email address strings.

    Returns:
        List[str]: List of valid, normalized (lowercase) email addresses.
    """
    # Regular expression components:
    # Local part: one or more of [a-zA-Z0-9._-], but non-empty
    # Domain: one or more labels separated by dots
    # Each label: alphanumeric and hyphens, but not starting or ending with hyphen
    # TLD: 2 to 6 alphabetic characters

    label = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
    domain_pattern = rf"(?:{label}\.)+[A-Za-z]{{2,6}}"
    email_pattern = rf"^[A-Za-z0-9._-]+@{domain_pattern}$"
    email_regex = re.compile(email_pattern)

    normalized_valid_emails = []
    for email in emails:
        if not isinstance(email, str):
            continue
        email = email.strip()
        if email_regex.fullmatch(email):
            normalized_valid_emails.append(email.lower())

    return normalized_valid_emails


def main():
    input_emails = [
        "User.Name@example.com",
        "invalid-email@",
        "test@sub-domain.example.co",
        "bad@domain-.com",
    ]

    output = validate_and_normalize_emails(input_emails)
    print(output)


if __name__ == "__main__":
    main()
```