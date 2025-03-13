def find_common(list1, list2):
    """
    Find and return a list of unique elements common to both input lists.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list of unique elements that appear in both input lists,
              preserving the order of first occurrence in list1
    
    Notes:
        - Returns an empty list if no common elements are found
        - Handles lists of any hashable type
        - Handles empty lists
        - Removes duplicate common elements
    """
    # Convert list2 to a set for efficient lookup
    set2 = set(list2)
    
    # Use a dict to preserve order and remove duplicates
    unique_common = {}
    for item in list1:
        if item in set2:
            # Only add the first occurrence of each common item
            unique_common.setdefault(item, None)
    
    return list(unique_common.keys())