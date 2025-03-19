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
    non_empty_arrays = [arr for arr in input_array if arr]
    
    # Result and tracking
    result = []
    seen = set()
    
    # Extremely precise traversal
    for arr in reversed(non_empty_arrays):
        # Reverse the current array
        reversed_arr = list(reversed(arr))
        
        # Unique tracking with special rules
        unique_temp = []
        for item in reversed_arr:
            if item not in seen:
                unique_temp.append(item)
                seen.add(item)
        
        # Prepend unique items
        result = unique_temp + result
    
    return result