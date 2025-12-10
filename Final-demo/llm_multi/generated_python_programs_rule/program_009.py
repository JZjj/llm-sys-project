```python
#!/usr/bin/env python3
"""
This script filters prime numbers from a list of non-negative integers.
Users can input a sequence of integers separated by spaces via the command line.
Invalid inputs are handled gracefully with error messages.
"""

import sys
import math


def is_prime(n: int) -> bool:
    """
    Efficiently checks if an integer n is prime.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: list[int]) -> list[int]:
    """
    Takes a list of integers and returns a new list containing only the prime numbers.
    """
    return [num for num in numbers if is_prime(num)]


def parse_input(input_str: str) -> list[int]:
    """
    Parses a string of space-separated values into a list of non-negative integers.
    Raises ValueError if any token is not a valid non-negative integer without leading zeros (except zero itself).
    """
    tokens = input_str.strip().split()
    if not tokens:
        raise ValueError("No input detected.")
    numbers = []
    for token in tokens:
        # Reject tokens with signs or leading zeros (except '0')
        if token.startswith(('+', '-')):
            raise ValueError(f"Invalid integer token: '{token}' (signed integers not allowed).")
        if len(token) > 1 and token.startswith('0'):
            # Leading zeros not allowed except for '0'
            raise ValueError(f"Invalid integer token: '{token}' (leading zeros not allowed).")
        try:
            num = int(token, 10)
        except ValueError:
            raise ValueError(f"Invalid integer token: '{token}'. Please enter non-negative integers only.")
        numbers.append(num)
    return numbers


def main() -> None:
    """
    Main function to handle CLI input and output.
    """
    print("Enter a sequence of non-negative integers separated by spaces:")
    try:
        input_str = sys.stdin.readline()
        numbers = parse_input(input_str)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    primes = filter_primes(numbers)
    print("Prime numbers:", ' '.join(map(str, primes)))


if __name__ == "__main__":
    main()
```