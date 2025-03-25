def sort_nums(numbers):
    """
    Initial sorting function with a known bug.
    
    This function intentionally has a performance issue and may not correctly 
    sort all input lists.
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: A potentially incorrectly sorted list of numbers
    """
    # Intentionally inefficient bubble sort with a potential bug
    n = len(numbers)
    for i in range(n):
        # Deliberate bug: not swapping correctly
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j] = numbers[j+1]  # Incorrect swap
    return numbers

def optimal_sort(numbers):
    """
    Optimized sorting function with improved time complexity.
    
    Uses the built-in Timsort algorithm which has O(n log n) time complexity.
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: A correctly sorted list of numbers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Type checking
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("List must contain only numeric elements")
    
    # Use Python's built-in sorted function which uses Timsort
    return sorted(numbers)