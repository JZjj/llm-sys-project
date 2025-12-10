def group_emails_by_domain(email_list):
    """
    Groups email addresses by their domain names.

    Args:
        email_list (list of str): List of email addresses.

    Returns:
        dict: Dictionary with domain names as keys and lists of usernames as values.
    """
    grouped = {}
    for email in email_list:
        if not isinstance(email, str):
            continue  # Ignore non-string entries

        email = email.strip()
        if email.count('@') != 1:
            continue  # Ignore invalid email formats

        username, domain = email.split('@')
        username = username.strip()
        domain = domain.strip()
        if not username or not domain:
            continue  # Ignore if username or domain is empty

        grouped.setdefault(domain, []).append(username)

    return grouped


if __name__ == "__main__":
    emails = [
        "alice@example.com",
        "bob@example.com",
        "carol@test.org",
        "dave@example.com",
        "eve@test.org",
        "invalidemail.com",
        "foo@bar@baz.com",
        "@missingusername.com",
        "missingdomain@",
        "normal.user@domain.com"
    ]

    grouped_emails = group_emails_by_domain(emails)
    for domain, users in grouped_emails.items():
        print(f"{domain}: {users}")