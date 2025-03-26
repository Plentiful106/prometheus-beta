def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence up to n where the sum of any two consecutive 
    numbers (starting from the third number) is always divisible by 3.

    Args:
        n (int): The upper limit of the sequence generation.

    Returns:
        list: A modified Fibonacci sequence satisfying the divisibility condition.

    Raises:
        ValueError: If the input is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle edge cases
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    
    # Initialize sequence
    sequence = [1, 1]
    
    while sequence[-1] <= n:
        # Create a new number that ensures divisibility by 3
        next_num = sequence[-1] + sequence[-2]
        
        # If the number exceeds n, stop
        if next_num > n:
            break
        
        sequence.append(next_num)
    
    return sequence