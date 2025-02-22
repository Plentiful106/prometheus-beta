def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        list: A list of missing numbers between the smallest and largest numbers
    
    Raises:
        ValueError: If the input array is empty or None
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Find the minimum and maximum values in the array
    min_val = arr[0]
    max_val = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_val + 1, max_val) 
        if num not in num_set
    ]
    
    return missing_numbers