def is_prime(n: int) -> bool:
    """Check if a number is prime."""
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
    Takes a list of integers and returns a new list containing only the prime numbers,
    sorted in ascending order.
    
    :param numbers: List of integers
    :return: Sorted list of prime integers
    :raises TypeError: If input is not a list of integers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError("All elements in the list must be integers.")
    
    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage
    example_list = [15, 3, 5, 8, 11, 4, 13, 9, 1, 0, -7, 17]
    try:
        primes = filter_and_sort_primes(example_list)
        print(f"Original list: {example_list}")
        print(f"Primes sorted: {primes}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()