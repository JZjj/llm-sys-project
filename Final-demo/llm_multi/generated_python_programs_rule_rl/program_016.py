import math
from bisect import bisect_left

def sieve_primes(n):
    """Generate a set of prime numbers up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return set()
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return {i for i, prime in enumerate(sieve) if prime}

def longest_prime_diff_subsequence(arr):
    """
    Returns the length of the longest subsequence where elements are strictly increasing
    and the difference between consecutive elements is a prime number.
    """
    n = len(arr)
    if n == 0:
        return 0

    max_val = max(arr)
    min_val = min(arr)
    max_diff = max_val - min_val
    if max_diff < 2:
        # Differences less than 2 cannot be prime
        return 0

    primes = sieve_primes(max_diff)

    value_indices = {}
    for idx, val in enumerate(arr):
        value_indices.setdefault(val, []).append(idx)

    dp = [1] * n

    for i in range(n):
        current_val = arr[i]
        for p in primes:
            prev_val = current_val - p
            if prev_val in value_indices:
                indices_list = value_indices[prev_val]
                pos = bisect_left(indices_list, i)
                if pos > 0:
                    j = indices_list[pos - 1]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

    max_len = max(dp)
    return max_len if max_len > 1 else 0

if __name__ == "__main__":
    example_input = [1, 3, 5, 8, 13, 18, 23]
    result = longest_prime_diff_subsequence(example_input)
    print(result)  # Expected output: 5