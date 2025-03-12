def get_prime_factors(n):
    """
    Calculate the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A sorted list of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor^2 <= n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # If not divisible, increment divisor
            divisor += 1
    
    # If n is greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors