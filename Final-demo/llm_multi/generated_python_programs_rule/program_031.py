```python
import re
from collections import defaultdict

def group_emails_by_domain(emails):
    """
    Groups email addresses by their domain (case-insensitive).
    Invalid email formats are skipped silently.

    :param emails: List of email address strings.
    :return: Dictionary with lowercase domain as keys and list of emails as values.
    """
    domain_map = defaultdict(list)

    # Regex for basic email validation: local@domain
    # This regex checks basic email structure but does not cover all RFC 5322 details for simplicity.
    email_pattern = re.compile(r"^[^@\s]+@([^@\s]+\.[^@\s]+)$")

    for email in emails:
        if not isinstance(email, str):
            continue

        match = email_pattern.match(email.strip())
        if match:
            domain = match.group(1).lower()
            domain_map[domain].append(email)

    return dict(domain_map)


def main():
    # Sample usage and demonstration
    input_emails = [
        "User1@example.com",
        "user2@Example.com",
        "admin@test.org",
        "invalidemail@",
        "noatsymbol.com",
        None,
        12345,
        "user3@EXAMPLE.COM"
    ]

    grouped = group_emails_by_domain(input_emails)
    for domain, emails in grouped.items():
        print(f"{domain}: {emails}")


if __name__ == "__main__":
    main()
```