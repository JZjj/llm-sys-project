```python
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter out prime numbers from the given list and return them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    # Example usage and simple test cases
    test_cases = [
        [],
        [0, 1, -3, 2, 3, 4, 5, 16, 17, 19, 23, 24, 29],
        [10, 11, 12, 13, 14, 15, 16, 17],
        [-7, -5, -3, -2, -1, 0, 1],
        [2],
        [999983, 999979, 999961, 4, 6, 8]
    ]

    for i, case in enumerate(test_cases, 1):
        result = filter_primes(case)
        print(f"Test case {i}: Input: {case}")
        print(f"           Primes: {result}\n")


if __name__ == "__main__":
    main()
```