```python
#!/usr/bin/env python3
"""
This module provides a function to filter prime numbers from a list of integers,
returning a sorted list of primes. It includes robust type checking and uses an
efficient prime checking algorithm suitable for large inputs.
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using 6k±1 optimization.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from a list of integers and return them sorted.

    Args:
        numbers (List[int]): The list of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for idx, elem in enumerate(numbers):
        if not isinstance(elem, int):
            raise TypeError(
                f"All elements must be integers. Element at index {idx} is of type {type(elem).__name__}."
            )

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage and basic test cases
    test_cases = [
        [10, 2, 3, 5, 8, 13, 17, 19, 23, 24],
        [0, 1, -3, -5, 2, 3],
        [],
        [4, 6, 8, 9, 10],
        [7919, 7877, 7907, 7879],  # large primes
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            result = filter_primes(case)
        except TypeError as e:
            print(f"Test case {i} raised an exception: {e}")
        else:
            print(f"Test case {i}: input={case}\n  primes={result}\n")


if __name__ == "__main__":
    main()
```