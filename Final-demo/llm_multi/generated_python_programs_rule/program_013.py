```python
#!/usr/bin/env python3
"""
A Python program that defines a function to filter prime numbers from a list of integers.
The function is efficient for lists containing up to 10,000 integers and handles edge cases.
Includes input validation and error handling.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter and return prime numbers from the input list.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: List containing only prime numbers from the input.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list, got {type(numbers).__name__} instead.")

    primes = []
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {idx} is not an integer: {num!r}")
        if is_prime(num):
            primes.append(num)

    return primes


def main():
    # Example usage and simple interactive test:
    import sys

    print("Enter a list of integers separated by spaces (or press Enter for an empty list):")
    user_input = sys.stdin.readline().strip()

    if user_input == "":
        input_list = []
    else:
        try:
            input_list = [int(x) for x in user_input.split()]
        except ValueError as e:
            print(f"Error: all inputs must be integers. {e}")
            sys.exit(1)

    try:
        primes = filter_primes(input_list)
    except TypeError as e:
        print(f"Input error: {e}")
        sys.exit(1)

    if primes:
        print("Prime numbers in the list:", primes)
    else:
        print("No prime numbers found in the list.")


if __name__ == "__main__":
    main()
```