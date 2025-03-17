def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer 
        b (int): Second integer

    Returns:
        int: The greatest common divisor of a and b

    Raises:
        TypeError: If inputs are not integers
        ValueError: If either input is negative
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Handle negative inputs
    a, b = abs(a), abs(b)
    
    # Handle zero case
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a