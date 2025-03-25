def reverse_list(input_list):
    """
    Reverse a list of integers without using built-in list manipulation functions.
    
    Args:
        input_list (list): A list of integers to be reversed.
    
    Returns:
        list: A new list with elements in reverse order.
    
    Raises:
        TypeError: If input is not a list.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Create a new list to store reversed elements
    reversed_list = []
    
    # Manually iterate through the input list from end to beginning
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    
    return reversed_list