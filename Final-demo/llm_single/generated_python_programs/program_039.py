import sys

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

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def filter_and_sort_primes(numbers):
    """
    Filters the list to include only prime numbers and returns them sorted.

    Args:
        numbers (list): List of integers.

    Returns:
        list: Sorted list of prime numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    # Validate all elements are integers
    for idx, num in enumerate(numbers):
        if not isinstance(num, int):
            raise ValueError(f"Element at index {idx} is not an integer.")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes

def main():
    """
    Example usage of filter_and_sort_primes function.
    """
    example_lists = [
        [10, 17, 4, 23, 8, 29, 1, 0, -3],
        [4, 6, 8, 10],
        [],
        [2, 3, 5, 7, 11],
        [15, 21, 22, 23]
    ]

    for idx, lst in enumerate(example_lists, start=1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Example {idx}: Input: {lst}\nPrime numbers sorted: {primes}\n")
        except (TypeError, ValueError) as e:
            print(f"Example {idx}: Error processing list {lst}: {e}\n")

if __name__ == "__main__":
    main()