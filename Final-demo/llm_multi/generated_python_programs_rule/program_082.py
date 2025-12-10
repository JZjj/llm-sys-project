```python
#!/usr/bin/env python3
"""
This module provides functionality to filter prime numbers from a list of integers.
"""

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.

    Raises:
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int for n, got {type(n).__name__}")
    if n < 2:
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


def filter_primes(numbers):
    """
    Filter prime numbers from the input list and return them sorted.

    Args:
        numbers (list): List of integers.

    Returns:
        list: Sorted list of prime numbers from the input list.

    Raises:
        TypeError: If numbers is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected list for numbers, got {type(numbers).__name__}")

    for idx, item in enumerate(numbers):
        if not isinstance(item, int):
            raise TypeError(f"All elements must be integers. Element at index {idx} is {type(item).__name__}")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage and simple test cases
    test_cases = [
        [3, 4, 5, 6, 7, 8, 9, 10],
        [13, 17, 19, 23, 29, 31],
        [1, 0, -3, 2, 3],
        [],
        [2],
        [15, 21, 25, 27]
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            result = filter_primes(case)
            print(f"Test case {i}: Input: {case} => Primes: {result}")
        except Exception as e:
            print(f"Test case {i}: Input: {case} => Raised exception: {e}")


if __name__ == "__main__":
    main()
```