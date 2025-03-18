def symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a set of elements which are in either of the lists,
    but not in their intersection.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list containing elements that are in either list1 or list2, but not both
    
    Raises:
        TypeError: If input arguments are not lists
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")
    
    # Convert lists to sets to use set operations
    set1 = set(list1)
    set2 = set(list2)
    
    # Compute symmetric difference and convert back to a list
    symmetric_diff_set = set1.symmetric_difference(set2)
    
    return list(symmetric_diff_set)