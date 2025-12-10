```python
#!/usr/bin/env python3
"""
Module to filter valid IPv4 addresses from a list of strings.
A valid IPv4 address consists of four decimal numbers (0-255) separated by dots,
with no leading zeros except for zero itself.
"""

from typing import List


def is_valid_ipv4(ip: str) -> bool:
    """
    Check if the given string is a valid IPv4 address.

    Args:
        ip: The string to validate as IPv4 address.

    Returns:
        True if ip is a valid IPv4 address, False otherwise.
    """
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        # Check leading zeros:
        if len(part) > 1 and part[0] == '0':
            return False
        num = int(part)
        if num > 255:
            return False
    return True


def filter_valid_ipv4_addresses(addresses: List[str]) -> List[str]:
    """
    Filters the list of strings returning only valid IPv4 addresses.

    Args:
        addresses: List of strings to filter.

    Returns:
        List of strings containing only valid IPv4 addresses.
    """
    return [ip for ip in addresses if is_valid_ipv4(ip)] if addresses else []


def main():
    # Example usage and testing
    test_addresses = [
        "192.168.1.1",
        "256.100.50.0",
        "192.168.01.1",
        "abc.def.ghi.jkl",
        "0.0.0.0",
        "255.255.255.255",
        "1.2.3.4",
        "01.2.3.4",
        "123.045.067.089",
        ""
    ]
    valid_ips = filter_valid_ipv4_addresses(test_addresses)
    print("Valid IPv4 addresses:")
    for ip in valid_ips:
        print(ip)


if __name__ == "__main__":
    main()
```