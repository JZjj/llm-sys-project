```python
#!/usr/bin/env python3
"""
Program to filter prime numbers from a list of integers,
returning them sorted in ascending order.

Includes efficient primality checking and robust input validation.
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
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # Check only up to sqrt(n), testing divisors of form 6k±1
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """
    Filter the prime numbers from the input list and return them sorted ascending.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers from input.

    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for idx, element in enumerate(numbers):
        if not isinstance(element, int):
            raise TypeError(
                f"All elements must be integers. Element at index {idx} is of type {type(element).__name__}."
            )

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    # Example usage and simple test cases

    test_cases = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10],
        [13, 29, 15, 23, 4, 1, 0, -3, 17],
        [],
        [0, 1, -1, -5],
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            result = filter_primes(case)
            print(f"Test case #{i}: Input: {case}")
            print(f"Prime numbers sorted: {result}\n")
        except Exception as e:
            print(f"Test case #{i} raised an exception: {e}")

    # Example of invalid input to demonstrate error handling
    invalid_inputs = [
        None,
        "string",
        [2, 3, "5"],
        [2.0, 3],
    ]
    for i, invalid in enumerate(invalid_inputs, 1):
        try:
            filter_primes(invalid)
        except Exception as e:
            print(f"Invalid input test #{i} correctly raised an exception: {e}")


if __name__ == "__main__":
    main()
```