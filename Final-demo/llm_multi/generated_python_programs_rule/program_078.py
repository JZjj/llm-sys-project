```python
#!/usr/bin/env python3
from typing import List, Dict


def group_emails_by_domain(emails: List[str]) -> Dict[str, List[str]]:
    """
    Groups emails by their domain names, ignoring case differences in domains.

    Args:
        emails: List of email address strings.

    Returns:
        Dictionary with lowercase domain names as keys and list of original emails as values.
    """
    grouped = {}
    for email in emails:
        # Validate: exactly one '@'
        if email.count('@') != 1:
            continue
        local_part, domain_part = email.rsplit('@', 1)
        # Basic sanity check: domain and local parts must not be empty and domain must contain at least one dot
        if not local_part or not domain_part or '.' not in domain_part:
            continue
        domain_key = domain_part.lower()
        grouped.setdefault(domain_key, []).append(email)
    return grouped


def main():
    # Example input
    emails = [
        "alice@example.com",
        "bob@Example.com",
        "charlie@test.org",
        "invalidemail@",
        "dave@example.com",
    ]
    result = group_emails_by_domain(emails)
    print(result)


if __name__ == "__main__":
    main()
```