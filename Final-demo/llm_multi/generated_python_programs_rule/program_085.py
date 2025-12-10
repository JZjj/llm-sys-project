```python
#!/usr/bin/env python3

def validate_and_normalize_ipv4(addresses):
    """
    Validate and normalize a list of IPv4 address strings.

    Args:
        addresses (list[str]): List of strings representing potential IPv4 addresses.

    Returns:
        list[str]: Sorted list of normalized valid IPv4 addresses.
    """
    valid_addresses = []

    for addr in addresses:
        octets = addr.split(".")
        if len(octets) != 4:
            continue

        normalized_octets = []
        valid = True
        for octet in octets:
            # Check if octet is non-empty and all digits
            if not octet.isdigit():
                valid = False
                break

            num = int(octet)
            if num > 255:
                valid = False
                break

            normalized_octets.append(str(num))

        if valid:
            normalized_addr = ".".join(normalized_octets)
            valid_addresses.append(normalized_addr)

    return sorted(valid_addresses, key=lambda ip: [int(o) for o in ip.split(".")])


def main():
    input_addresses = ["192.168.001.001", "256.100.50.0", "10.0.0.01", "abc.def.ghi.jkl"]

    output = validate_and_normalize_ipv4(input_addresses)
    print(output)


if __name__ == "__main__":
    main()
```