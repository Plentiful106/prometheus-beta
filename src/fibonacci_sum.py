def fibonacci_sequence_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci terms to sum.
    
    Returns:
        int: The sum of the first n numbers in the Fibonacci sequence.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return 0
    
    # Initialize Fibonacci sequence variables
    a, b = 0, 1
    total_sum = 0
    
    # Calculate sum of first n Fibonacci numbers
    for _ in range(n):
        total_sum += a
        a, b = b, a + b
    
    return total_sum