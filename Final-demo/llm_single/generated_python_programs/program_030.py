def is_prime(n: int) -> bool:
    """Check if a number is a prime number.
    
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
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_sorted_primes(numbers):
    """Filter prime numbers from the list and return them sorted.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        list: Sorted list of prime numbers.
        
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")
    
    primes = [num for num in numbers if is_prime(num)]
    return sorted(primes)


def main():
    """Main function for example usage."""
    example_list = [10, 15, 3, 7, 2, 9, 11, -5, 0, 1]
    try:
        primes = get_sorted_primes(example_list)
        print(f"Original list: {example_list}")
        print(f"Prime numbers sorted: {primes}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()