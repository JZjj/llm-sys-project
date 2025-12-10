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
    Takes a list of integers and returns a sorted list of prime numbers.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        list: Sorted list of prime numbers from the input list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    
    primes = []
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the input list must be integers.")
        if is_prime(num):
            primes.append(num)
    return sorted(primes)


def main():
    """Example usage of filter_and_sort_primes."""
    example_list = [10, 3, 5, 8, 23, 4, 1, 0, -7, 17]
    try:
        primes = filter_and_sort_primes(example_list)
        print("Prime numbers sorted:", primes)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()