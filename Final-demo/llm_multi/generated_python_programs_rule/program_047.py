```python
#!/usr/bin/env python3
"""
Program to filter prime numbers from a list of integers,
preserving their order.

The primality check uses a deterministic method suitable for large inputs,
and the code avoids common vulnerabilities.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    Handles large integers correctly.

    Args:
        n: Integer to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # alternates between adding 2 and 4 (checks 6k ± 1)
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Returns a new list containing only primes from the input list.

    Args:
        numbers: List of integers.

    Returns:
        List of prime integers in their original order.
    """
    return [num for num in numbers if is_prime(num)]


def main():
    """
    Example run: reads integers from user input, space separated,
    filters primes and prints them.
    """
    try:
        input_str = input("Enter integers separated by space: ").strip()
        if not input_str:
            print("No input provided.")
            return

        tokens = input_str.split()
        numbers = []
        for token in tokens:
            # Accept tokens representing valid integers without extra chars
            # Handle optional leading + or - sign followed by digits only
            if token and (token[0] in '+-' and token[1:].isdigit() or token.isdigit()):
                try:
                    num = int(token)
                    numbers.append(num)
                except ValueError:
                    # skip invalid token
                    continue

        if not numbers:
            print("No valid integers provided.")
            return

        primes = filter_primes(numbers)
        print("Prime numbers:", primes)

    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")


if __name__ == "__main__":
    main()
```