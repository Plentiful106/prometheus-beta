def longest_subarray_max_diff(A, k):
    """
    Find the length of the longest subarray where the absolute difference 
    between adjacent elements is greater than or equal to a given value k.

    Args:
        A (list): A list of integers
        k (int): The minimum absolute difference required between adjacent elements

    Returns:
        int: Length of the longest valid subarray

    Raises:
        ValueError: If input array is empty or k is negative
    """
    # Input validation
    if not A:
        raise ValueError("Input array cannot be empty")
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    
    # If array has only one element, return 1
    if len(A) == 1:
        return 1
    
    # Initialize variables
    max_length = 1
    current_length = 1
    
    # Iterate through the array and track subarray lengths
    for i in range(1, len(A)):
        # Check absolute difference between current and previous element
        if abs(A[i] - A[i-1]) >= k:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length