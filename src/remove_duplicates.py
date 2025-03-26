def remove_duplicates(numbers):
    """
    Remove duplicate integers from a list while preserving the original order.
    
    Args:
        numbers (list): A list of integers 
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order of first occurrence
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If the list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers 
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Use a set to track seen numbers while preserving order
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result