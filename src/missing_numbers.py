def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers 
                    (can be in ascending or descending order).
    
    Returns:
        list: A sorted list of missing numbers between the minimum 
              and maximum values in the input array.
    
    Raises:
        ValueError: If the input is not a list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] <= arr[-1]
    
    # Sort the array in ascending order if it's descending
    if not is_ascending:
        arr = sorted(arr, reverse=True)
    
    # Find the minimum and maximum
    max_num = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Special case for single element array
    if len(arr) == 1:
        missing = list(range(1, arr[0]))
        return missing if is_ascending else missing[::-1]
    
    # For large gaps or other cases
    missing = [
        num for num in range(arr[0], max_num) 
        if num not in num_set
    ]
    
    # If the original array was descending, reverse the missing numbers
    return sorted(missing, reverse=not is_ascending)