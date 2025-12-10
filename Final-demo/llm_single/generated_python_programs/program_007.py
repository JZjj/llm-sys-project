import math
from typing import List

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check divisibility up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filters the prime numbers from the input list and returns them sorted.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers, or empty list if none found.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)

def main():
    """
    Main function to demonstrate example usage.
    """
    example_lists = [
        [10, 3, 5, 8, 2, 7, 11, 13],
        [4, 6, 8, 10],
        [-3, 0, 1, 2, 3],
        [],
        [17, 19, 23, 29, 31]
    ]

    for idx, numbers in enumerate(example_lists, 1):
        try:
            primes = filter_and_sort_primes(numbers)
            print(f"Example {idx}: Input: {numbers}")
            print(f"          Primes: {primes}\n")
        except Exception as e:
            print(f"Example {idx}: Error processing input: {e}\n")

if __name__ == "__main__":
    main()