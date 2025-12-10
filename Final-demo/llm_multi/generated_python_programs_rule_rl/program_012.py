import math
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
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filter the list to include only prime numbers and return them sorted.
    """
    # Use set to avoid duplicates and improve performance on large lists
    unique_numbers = set(numbers)
    primes = [num for num in unique_numbers if is_prime(num)]
    primes.sort()
    return primes

if __name__ == "__main__":
    sample_numbers = [29, 15, 3, 8, 23, 42, 17, 4, 2, 1, 0, -7, 97]
    primes = filter_and_sort_primes(sample_numbers)
    print("Prime numbers sorted:", primes)