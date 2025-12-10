import math
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for factors up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_and_sort_primes(numbers: List[int]) -> List[int]:
    """
    Filter prime numbers from the list and return them sorted.
    
    Args:
        numbers (List[int]): List of integers.
    
    Returns:
        List[int]: Sorted list of prime numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All items in the input list must be integers.")
    
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    # Example usage
    example_lists = [
        [10, 3, 5, 8, 13, 21],
        [4, 6, 8, 10],
        [-3, 0, 2, 17, 19, 23],
        [],
        [29, 29, 2, 3, 3]
    ]
    
    for i, lst in enumerate(example_lists, start=1):
        try:
            result = filter_and_sort_primes(lst)
            print(f"Example {i}: Input: {lst}\n  Primes: {result}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {i}: Input: {lst}\n  Error: {e}\n")

if __name__ == "__main__":
    main()