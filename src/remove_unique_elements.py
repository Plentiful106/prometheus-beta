def remove_unique_elements(my_list):
    """
    Remove duplicate values from a list of integers using only built-in list methods.
    
    Args:
        my_list (list): A list of integers to process.
    
    Returns:
        list: A new list containing only the elements that appear more than once.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in my_list):
        raise TypeError("All list elements must be integers")
    
    # Use list comprehension to keep only elements that appear more than once
    return [x for x in my_list if my_list.count(x) > 1]