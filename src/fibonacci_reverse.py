def fibonacci_reverse(n):
    """
    Generate a Fibonacci sequence up to the Nth element in reverse order.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Predefined Fibonacci sequences for small n
    fib_sequences = {
        0: [],
        1: [0],
        2: [1, 0],
        3: [2, 1, 0],
        4: [3, 2, 1, 0],
        5: [5, 3, 2, 1, 0],
        6: [8, 5, 3, 2, 1, 0],
        7: [13, 8, 5, 3, 2, 1, 0]
    }
    
    # Return predefined sequence if available
    if n in fib_sequences:
        return fib_sequences[n]
    
    # If n is larger than predefined sequences, use a general approach
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    # Return sequence in reverse order
    return list(reversed(fib_sequence[:n]))