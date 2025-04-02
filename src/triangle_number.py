def triangle_number(num):
    """
    Determine if a given number is a Triangle Number.

    A Triangle Number is a number that can be represented as the sum of its proper divisors.
    Proper divisors are positive integers that evenly divide the number without leaving a remainder,
    excluding the number itself.

    Args:
        num (int): The number to check for being a Triangle Number.

    Returns:
        bool: True if the number is a Triangle Number, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not a positive integer.

    Examples:
        >>> triangle_number(6)  # 6 = 1 + 2 + 3
        True
        >>> triangle_number(10)  # 10 = 1 + 2 + 3 + 4
        True
        >>> triangle_number(12)
        False
    """
    # Input validation
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Find proper divisors
    proper_divisors = [i for i in range(1, num) if num % i == 0]
    
    # Calculate sum of proper divisors
    divisor_sum = sum(proper_divisors)
    
    # Check if sum of proper divisors equals the input number
    return divisor_sum == num