```python
#!/usr/bin/env python3
"""
This module provides a function to filter prime numbers from a list and return them sorted ascendingly.
It includes input validation and uses an efficient primality checking algorithm.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using an efficient method.
    Args:
        n (int): The number to check.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are primes
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filters prime numbers from the input list and returns them sorted in ascending order.
    Args:
        numbers (List[int]): List of integers to filter.
    Returns:
        List[int]: Sorted list of prime numbers.
    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    for index, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"All items in the list must be integers. Invalid item at index {index}: {item}")

    primes = [num for num in numbers if is_prime(num)]

    primes.sort()
    return primes


def main():
    # Example usage and simple test harness
    test_lists = [
        [10, 29, 15, 2, 3, 17, 20, 4],
        [1, 0, -5, 7, 11, 13],
        [],
        [4, 6, 8, 9, 10],
        list(range(1, 101)),
    ]

    for i, lst in enumerate(test_lists, 1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Test case {i}: Input: {lst}")
            print(f"Prime numbers: {primes}\n")
        except Exception as e:
            print(f"Test case {i} raised an exception: {e}\n")


if __name__ == "__main__":
    main()
```