import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Check if a number is a prime number.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Test divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from the list and return them sorted in ascending order.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of primes found in the input list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    # Validate all elements are integers
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the input list must be integers.")

    primes = [num for num in numbers if is_prime(num)]

    return sorted(primes)

def main():
    """
    Example usage of filter_and_sort_primes function.
    """
    example_lists = [
        [10, 15, 3, 7, 2, 11, 4],
        [8, 4, 6, 10],
        [-3, 0, 1, 13, 17, 19],
        []
    ]

    for idx, lst in enumerate(example_lists, start=1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Example {idx}: Input: {lst}")
            print(f"           Primes: {primes}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Error processing list {lst}: {e}")

if __name__ == "__main__":
    main()