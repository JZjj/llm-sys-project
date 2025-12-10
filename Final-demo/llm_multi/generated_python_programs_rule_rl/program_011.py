def group_emails_by_domain(emails):
    """
    Groups valid email addresses by their domain names.

    Args:
        emails (list of str): List of email addresses.

    Returns:
        dict: Dictionary with domain names as keys and lists of emails as values.
    """
    grouped = {}
    for email in emails:
        # Validate email according to the simplified rules
        if email.count('@') != 1:
            continue
        local_part, domain_part = email.split('@', 1)
        if not local_part or not domain_part:
            continue
        if '.' not in domain_part:
            continue

        # Normalize domain to lowercase for grouping
        domain_key = domain_part.lower()

        # Append the original email preserving case and order
        grouped.setdefault(domain_key, []).append(email)
    return grouped


if __name__ == "__main__":
    # Example usage and simple test
    test_emails = [
        "Alice@example.com",
        "bob@Example.com",
        "charlie@sub.example.com",
        "invalidemail@",
        "noatsymbol.com",
        "david@domain",
        "eve@domain.com",
        "frank@domain.COM",
        "@missinglocal.com",
        "grace@domain.co.uk"
    ]

    grouped = group_emails_by_domain(test_emails)
    for domain, emails in grouped.items():
        print(f"{domain}: {emails}")