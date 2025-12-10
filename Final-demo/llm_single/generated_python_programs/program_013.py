def is_prime(n):
    """Check if a number is prime."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
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


def filter_sorted_primes(numbers):
    """
    Takes a list of integers and returns a new list containing only the prime numbers,
    sorted in ascending order.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    # Example usage
    example_list = [10, 3, 5, 8, 13, 4, 7, 11, 0, -3, 17]
    try:
        primes = filter_sorted_primes(example_list)
        print("Prime numbers sorted:", primes)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()