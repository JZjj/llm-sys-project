def is_prime(n: int) -> bool:
    """Check if a number is a prime."""
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
    Return a sorted list of prime numbers from the input list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: Sorted list of prime numbers from the input.
    
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All items in the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage of filter_and_sort_primes function
    try:
        example_list = [29, 15, 3, 8, 22, 7, 11, 1, -5, 0]
        primes = filter_and_sort_primes(example_list)
        print("Prime numbers sorted:", primes)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()