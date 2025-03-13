def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers.
    
    This function takes a sorted list of integers and returns a new list 
    with duplicate values removed, without using built-in functions like 
    set() or dict().
    
    Args:
        sorted_list (list): A sorted list of integers
    
    Returns:
        list: A new list with duplicate values removed, maintaining the 
              original sorted order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not sorted_list:
        return []
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("All elements must be integers")
    
    # Initialize result list with the first element
    result = [sorted_list[0]]
    
    # Iterate through the list, adding only unique elements
    for num in sorted_list[1:]:
        # Only add if different from the last element in result
        if num != result[-1]:
            result.append(num)
    
    return result