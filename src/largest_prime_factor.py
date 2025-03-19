def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of the input number.

    Raises:
        ValueError: If the input is less than or equal to 1.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Use the most efficient method to find largest prime factor
    largest_prime = 1
    
    # First, handle any 2 as a factor
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    
    # Check for odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_prime = factor
            n = n // factor
        factor += 2
    
    # If n is still greater than 2, it means n itself is prime
    if n > 2:
        largest_prime = n
    
    return largest_prime