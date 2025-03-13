def count_triangular_numbers(n):
    """
    Count the number of triangular numbers less than or equal to n.
    
    A triangular number is a number that can be represented as a triangular 
    pattern of points where the first row contains a single element and 
    each subsequent row contains one more element than the previous row.
    
    Triangular numbers follow the formula: T(k) = k * (k + 1) // 2
    
    Args:
        n (int): The upper limit to count triangular numbers.
    
    Returns:
        int: The count of triangular numbers less than or equal to n.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If n is 0, there are no triangular numbers
    if n == 0:
        return 0
    
    # Find the count of triangular numbers
    count = 0
    triangular_number = 0
    k = 1
    
    # Generate triangular numbers until they exceed n
    while triangular_number <= n:
        count += 1
        k += 1
        triangular_number = k * (k - 1) // 2
    
    return count - 1  # Subtract 1 to get the correct count