def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Returns True if n is prime, False otherwise.
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
    Filters prime numbers from a list and returns them sorted in ascending order.
    Args:
        numbers: list of integers
    Returns:
        list of prime integers sorted ascending
    Raises:
        TypeError: if input is not a list or contains non-integers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage
    example_lists = [
        [10, 17, 4, 23, 8, 5, 3, 11],
        [1, 4, 6, 8, 10],
        [],
        [2, 3, 5, 7, 11, 13],
        [0, -3, 17, 19, 22]
    ]

    for idx, lst in enumerate(example_lists, 1):
        try:
            primes = filter_and_sort_primes(lst)
            print(f"Example {idx}: Input: {lst}")
            print(f"Prime numbers sorted: {primes}\n")
        except Exception as e:
            print(f"Example {idx}: Error processing list {lst}: {e}\n")


if __name__ == "__main__":
    main()