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

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Takes a list of integers and returns a new list containing only the prime numbers,
    sorted in ascending order. Returns an empty list if no primes are found.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    # Ensure all elements are integers
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")
    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)

def main():
    # Example usage
    try:
        sample_data = [10, 3, 5, 8, 13, 21, 2, -7, 0, 17]
        primes = filter_and_sort_primes(sample_data)
        print(f"Original list: {sample_data}")
        print(f"Prime numbers sorted: {primes}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()