```python
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    Handles edge cases: n < 2 are not prime.

    Parameters:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def filter_and_sort_primes(nums: List[int]) -> List[int]:
    """
    Filters the prime numbers from the list and returns them sorted.

    Parameters:
        nums (List[int]): List of integers.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    return sorted(num for num in nums if is_prime(num))


def main():
    # Example usage and simple test cases
    test_cases = [
        [],
        [0, 1, -1, -5, 2, 3, 5, 7],
        [10, 15, 20, 23, 29, 31],
        [-10, -3, 4, 6, 8, 9, 11, 13],
        [997, 991, 983, 2, 3],
    ]

    for i, case in enumerate(test_cases, 1):
        result = filter_and_sort_primes(case)
        print(f"Test case {i}: Input: {case}\n  Primes: {result}\n")


if __name__ == "__main__":
    main()
```