```python
#!/usr/bin/env python3
"""
A Python program that filters prime numbers from a list of integers.

The main function `filter_primes`:
- Accepts a list of integers.
- Returns a new list containing only the prime numbers.
- Raises TypeError if the input is not a list.
- Raises TypeError if any element in the list is not an integer.

Primality test:
- Efficiently checks primality using 6k±1 optimization.
- Handles edge cases (numbers < 2, small primes).

Security considerations:
- Validates input types strictly to prevent unexpected behavior.
- Avoids use of eval or other unsafe operations.
- Does not use external libraries, only Python standard library.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n in (2, 3):
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
    Filters prime numbers from a list of integers.

    Args:
        numbers (List[int]): The list of integers to filter.

    Returns:
        List[int]: A list containing only the prime numbers from the input.

    Raises:
        TypeError: If input is not a list or any element is not an integer.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    primes = []
    for idx, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(f"Element at index {idx} is not an integer.")
        if is_prime(element):
            primes.append(element)
    return primes


def main():
    # Example usage and simple tests.
    test_cases = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19],
        [],
        [1, 0, -3, 29, 31, 37],
        [15, 21, 22, 23, 24, 25],
        [999983, 999979, 1000000],  # large primes and non-prime
    ]

    for i, case in enumerate(test_cases, start=1):
        try:
            primes = filter_primes(case)
            print(f"Test case {i}: Input: {case}")
            print(f"Prime numbers: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```