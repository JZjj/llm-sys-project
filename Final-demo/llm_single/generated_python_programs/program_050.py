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
    Filter prime numbers from the list and return them sorted.
    
    Args:
        numbers (list): List of integers.
    
    Returns:
        list: Sorted list of prime numbers.
    
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError("All elements of the list must be integers.")
    
    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    """Example usage of filter_and_sort_primes."""
    try:
        example_list = [29, 15, 3, 4, 2, 10, 17, 23, 1, -3, 0]
        primes = filter_and_sort_primes(example_list)
        print(f"Original list: {example_list}")
        print(f"Filtered and sorted primes: {primes}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()