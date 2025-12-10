import sys

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
    Return a list of prime numbers from the input list, sorted in ascending order.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        list: Sorted list of prime numbers.
        
    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError("All items in the list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)

def main():
    # Example usage
    try:
        example_list = [29, 15, 3, 8, 7, 4, 13, 2, 1, 0, -3]
        primes = filter_and_sort_primes(example_list)
        print(f"Original list: {example_list}")
        print(f"Sorted primes: {primes}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()