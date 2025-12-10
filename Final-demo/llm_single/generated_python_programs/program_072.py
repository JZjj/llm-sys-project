import sys
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Returns True if n is a prime number, False otherwise.
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
    Return a sorted list of prime numbers from the input list.
    If there are no primes, returns an empty list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    # Validate all items in the list are integers
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    """
    Example usage of filter_primes function.
    """
    example_lists = [
        [11, 4, 6, 7, 9, 13, 17, 18],
        [1, 4, 6, 8, 10],
        [],
        [2, 3, 5, 11, 23, 29],
        [-3, 0, 1, 2, 3],
    ]

    for idx, lst in enumerate(example_lists, start=1):
        try:
            primes = filter_primes(lst)
            print(f"Example {idx}: Input: {lst}\nPrime numbers (sorted): {primes}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Error processing input {lst}: {e}\n")


if __name__ == "__main__":
    main()