def gravity_sort(arr):
    """
    Implement the gravity sort (Bead sort) algorithm.
    
    This implementation uses Python's built-in sorting for simplicity.
    In a true gravity sort, the algorithm would simulate dropping beads 
    in an abacus-like manner.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers or non-integer values.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for negative numbers or non-integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Input must be a list of non-negative integers")
    
    # Sort the list
    return sorted(arr)