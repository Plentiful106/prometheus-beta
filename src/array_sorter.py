def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order, with even number squares sorted in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with special handling for even number squares
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Sort the entire array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_numbers = [num for num in sorted_arr if num % 2 == 0]
    odd_numbers = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort even number squares in descending order
    even_squares = sorted([num**2 for num in even_numbers], reverse=True)
    
    # Combine odd numbers and even squares
    result = odd_numbers + even_squares
    
    return result