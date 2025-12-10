import math
import sys


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
    # Only check up to sqrt(n)
    limit = int(math.isqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def extract_sorted_primes(numbers):
    """
    Extract prime numbers from the list and return them sorted.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        list[int]: Sorted list of prime numbers found in numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    primes = []
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")
        if is_prime(num):
            primes.append(num)

    return sorted(primes)


def main():
    """
    Main function demonstrating example usage.
    """
    try:
        example_list = [29, 10, 15, 3, 7, 8, 23, 4, -5, 0, 2]
        primes = extract_sorted_primes(example_list)
        print("Original list:", example_list)
        print("Sorted primes:", primes)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()