def transform_multi_array(input_array):
    """
    Transform a multi-dimensional array with very specific requirements:
    1. Remove empty sub-arrays
    2. Reverse the order of elements in each sub-array
    3. Flatten the array with a precise ordering
    4. Remove duplicates while maintaining a specific order

    Args:
        input_array (list): A multi-dimensional array to be transformed

    Returns:
        list: Transformed and deduplicated array
    """
    # Remove empty sub-arrays
    filtered_arrays = [arr for arr in input_array if arr]
    
    # Initialize for result tracking
    result = []
    seen = set()
    
    # Very precise traversal strategy
    for i in range(len(filtered_arrays) - 1, -1, -1):
        # Reverse current sub-array
        current_arr = list(reversed(filtered_arrays[i]))
        
        # Temporary for this iteration's unique items
        unique_items = []
        
        # Collect unique items from current array
        for item in current_arr:
            if item not in seen:
                unique_items.append(item)
                seen.add(item)
        
        # Prepend unique items to result
        result = unique_items + result
    
    return result