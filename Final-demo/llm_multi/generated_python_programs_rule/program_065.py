```python
#!/usr/bin/env python3
"""
This program defines a function to filter prime numbers from a list of integers.
It efficiently checks primality using a 6k ± 1 optimization.
The function returns a sorted list of primes in ascending order.
"""

from typing import List


def is_prime(n: int) -> bool:
    """
    Efficiently checks if n is a prime number.
    Uses 6k ± 1 optimization to reduce the number of checks.

    Args:
        n (int): The number to check for primality.

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
    Filters and returns a sorted list of prime numbers from the input list.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    # Use set to avoid duplicate primality checks and duplicates in output
    unique_numbers = set(numbers)
    primes = [num for num in unique_numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    # Example usage:
    # Read integers from user input (space separated)
    try:
        user_input = input("Enter integers separated by spaces: ")
        input_numbers = list(map(int, user_input.strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    primes = filter_primes(input_numbers)
    print("Prime numbers (sorted):", primes)


if __name__ == "__main__":
    main()
```