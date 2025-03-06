def get_primes_up_to_n(n: int) -> list[int]:
    """
    Return a list of all prime numbers from 1 to n (inclusive).
    
    Args:
        n (int): The upper limit for finding prime numbers.
    
    Returns:
        list[int]: A list of prime numbers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle small numbers
    if n < 2:
        return []
    
    # Use Sieve of Eratosthenes algorithm for efficiency
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]