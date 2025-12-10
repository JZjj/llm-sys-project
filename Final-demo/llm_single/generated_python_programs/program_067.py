import math
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
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to sqrt(n)
    max_divisor = int(math.isqrt(n))
    for i in range(5, max_divisor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filters prime numbers from a list and returns them sorted.

    Args:
        numbers (List[int]): List of integers to filter.

    Returns:
        List[int]: Sorted list of prime numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    primes = []
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All items in the input list must be integers.")
        if is_prime(num):
            primes.append(num)

    return sorted(primes)

def main():
    # Example usage
    example_lists = [
        [10, 3, 5, 6, 7, 11, 12],
        [4, 6, 8, 9, 10],
        [],
        [2, 2, 3, 3, 5, 5],
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Example {idx}: Input: {lst}")
            print(f"Prime numbers sorted: {primes}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {idx} raised an error: {e}\n")

if __name__ == "__main__":
    main()