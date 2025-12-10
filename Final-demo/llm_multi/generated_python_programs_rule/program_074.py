```python
#!/usr/bin/env python3
"""
Validate IPv4 addresses from a list of strings.

A valid IPv4 address consists of four decimal numbers, each ranging from 0 to 255,
separated by dots (e.g., "192.168.0.1").

This program includes a function to filter valid IPv4 addresses from a list of strings,
strictly validating the format without using regular expressions and handling edge cases 
such as leading zeros and extra spaces.

Author: Senior Python Engineer
Date: 2024-06
"""

from typing import List


def is_valid_ipv4_address(ip_str: str) -> bool:
    """
    Validate a single IPv4 address string.

    Args:
        ip_str (str): The string to validate as an IPv4 address.

    Returns:
        bool: True if ip_str is a valid IPv4 address, False otherwise.
    """
    if not isinstance(ip_str, str):
        return False

    ip = ip_str.strip()
    if not ip:
        return False

    # IPv4 must have exactly three dots
    if ip.count('.') != 3:
        return False

    parts = ip.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        # Reject empty parts or parts with spaces inside
        if not part or ' ' in part:
            return False

        # All characters must be digits
        if not part.isdigit():
            return False

        # Leading zeros are not allowed unless the part is exactly '0'
        if len(part) > 1 and part[0] == '0':
            return False

        num = int(part)
        if num < 0 or num > 255:
            return False

    return True


def filter_valid_ipv4_addresses(ip_list: List[str]) -> List[str]:
    """
    Filter the input list, returning only valid IPv4 addresses.

    Args:
        ip_list (List[str]): List of strings to validate.

    Returns:
        List[str]: List of valid IPv4 address strings.
    """
    if not isinstance(ip_list, list):
        raise TypeError("Input must be a list of strings.")

    valid_ips = []
    for ip_str in ip_list:
        if not isinstance(ip_str, str):
            # Skip non-string input safely
            continue
        if is_valid_ipv4_address(ip_str):
            valid_ips.append(ip_str.strip())
    return valid_ips


def main():
    # Example usage and test cases
    test_ips = [
        "192.168.0.1",
        "255.255.255.255",
        "0.0.0.0",
        "01.2.3.4",        # invalid, leading zero
        "192.168.1",       # invalid, less parts
        "192.168.1.1.1",   # invalid, more parts
        "192.168.1.a",     # invalid, non-digit
        " 192.168.0.1 ",   # valid, spaces stripped
        "192.168.00.1",    # invalid, leading zero
        "256.100.100.100", # invalid, out of range
        "192.168.1. 1",    # invalid, space inside part
        "",                # invalid, empty string
        "  ",              # invalid, spaces only
        None,              # invalid, not string
        12345,             # invalid, not string
        "0.0.0.00"         # invalid, leading zero in last part
    ]

    valid_ips = filter_valid_ipv4_addresses(test_ips)
    print("Valid IPv4 addresses:")
    for ip in valid_ips:
        print(f"- {ip}")


if __name__ == "__main__":
    main()
```