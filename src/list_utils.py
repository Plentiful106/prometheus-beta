def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list of elements that appear in both input lists
    
    Notes:
        - Returns an empty list if no common elements are found
        - Preserves the order of first occurrence in list1
        - Handles lists of any hashable type
        - Handles empty lists
    """
    # Convert list2 to a set for efficient lookup
    set2 = set(list2)
    
    # Use a list comprehension with set membership to find common elements
    # Preserve the order of first occurrence in list1
    return [item for item in list1 if item in set2]