```python
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    Returns True if n is a prime number, False otherwise.
    Assumes n is a positive integer greater than 1.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors from 5 to sqrt(n) skipping even numbers
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # alternates between adding 2 and 4
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filters the input list, returning a list of prime numbers only.
    Raises:
        TypeError: If input is not a list or elements are not integers.
        ValueError: If the input list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    if not numbers:
        raise ValueError("Input list must not be empty.")

    primes = []
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {idx} is not an integer.")
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    # Example usage and basic test
    test_lists = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [15, 21, 23, 29, 30],
        [],
        [1, 0, -3, 17],
        [2**31 - 1],
        [2, '3', 5],  # invalid element
    ]

    for idx, test_list in enumerate(test_lists, 1):
        print(f"Test case {idx}: Input: {test_list}")
        try:
            primes = filter_primes(test_list)
            print(f"Prime numbers: {primes}\n")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
```