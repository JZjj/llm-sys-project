def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
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


def filter_primes(numbers):
    """
    Filter prime numbers from a list and return them sorted.
    
    Args:
        numbers (list): List of integers.
        
    Returns:
        list: Sorted list of prime numbers.
        
    Raises:
        TypeError: If input is not a list or contains non-integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in the input list must be integers.")

    primes = [num for num in numbers if is_prime(num)]
    primes.sort()
    return primes


def main():
    # Example usage
    try:
        sample_list = [29, 15, 3, 8, 2, 10, 17, 23, 4]
        primes = filter_primes(sample_list)
        print("Original list:", sample_list)
        print("Prime numbers sorted:", primes)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()