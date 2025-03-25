def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using recursion.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Base case
    if b == 0:
        return a
    
    # Recursive case using Euclidean algorithm
    return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) using recursion.
    
    The LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
        ZeroDivisionError: If both inputs are zero
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Handle special cases
    if a == 0 and b == 0:
        raise ZeroDivisionError("LCM is undefined when both inputs are zero")
    
    # Take absolute values
    a, b = abs(a), abs(b)
    
    # If either number is zero, LCM is zero
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using GCD
    return abs(a * b) // gcd(a, b)