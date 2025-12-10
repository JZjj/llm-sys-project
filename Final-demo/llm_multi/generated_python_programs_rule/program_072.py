```python
def is_prime(n: int) -> bool:
    """
    Efficiently checks if a number is prime.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if not isinstance(n, int):
        return False
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


def filter_and_sort_primes(int_list):
    """
    Filters prime numbers from the input list and returns them sorted ascending.
    
    Args:
        int_list (list): List of integers.
        
    Returns:
        list: Sorted list of prime numbers.
        
    Raises:
        TypeError: If input is not a list.
        ValueError: If any element in the list is not an integer.
    """
    if not isinstance(int_list, list):
        raise TypeError(f"Expected input to be a list, got {type(int_list).__name__}")

    for idx, item in enumerate(int_list):
        if not isinstance(item, int):
            raise ValueError(
                f"List element at index {idx} is not an integer: {item} (type: {type(item).__name__})"
            )

    primes = [num for num in int_list if is_prime(num)]
    primes.sort()
    return primes


def main():
    import sys

    print("Enter integers separated by spaces:")

    try:
        user_input = input()
        elements = user_input.strip().split()
        int_list = [int(x) for x in elements]
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.", file=sys.stderr)
        sys.exit(1)

    try:
        primes = filter_and_sort_primes(int_list)
    except (TypeError, ValueError) as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(1)

    print("Prime numbers sorted in ascending order:")
    print(primes)


if __name__ == "__main__":
    main()
```