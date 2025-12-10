import sys

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

def filter_primes(numbers):
    """
    Given a list of integers, return a new list containing only the prime numbers,
    sorted in ascending order.
    Raises:
        TypeError: if input is not a list or elements are not integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements of the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)

def main():
    """
    Main function demonstrating example usage.
    """
    example_lists = [
        [10, 3, 5, 6, 7, 4, 11, 13],
        [4, 6, 8, 10, 12],
        [],
        [2, 2, 3, 3, 5, 5],
        [17, 19, 23, 29, 31],
        [-3, 0, 1, 2, 3]
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            print(f"Example {idx} input: {lst}")
            primes = filter_primes(lst)
            print(f"Example {idx} primes: {primes}\n")
        except Exception as e:
            print(f"Example {idx} raised an error: {e}\n")

if __name__ == "__main__":
    main()