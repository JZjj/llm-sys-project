```python
#!/usr/bin/env python3
"""
This module provides a function to filter prime numbers from a list of integers.
Includes input validation and an efficient primality test without external libraries.
"""

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


def filter_primes(numbers):
    """
    Filter prime numbers from a list of integers.

    Args:
        numbers (list): List of integers.

    Returns:
        list: A new list containing only prime numbers from the input list.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(
                f"All elements must be integers. Element at index {idx} is of type {type(item).__name__}."
            )

    return [num for num in numbers if is_prime(num)]


def main():
    """Example usage and basic tests."""
    test_cases = [
        [],  # empty list
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [-10, -3, -2, 2, 3, 5],
        [11, 13, 17, 19, 23],
        [15, 21, 25, 27, 29, 31],
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            primes = filter_primes(case)
            print(f"Test case {i}: Input: {case}\n  Primes: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```