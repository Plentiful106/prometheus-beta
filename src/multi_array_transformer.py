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
    # Thoroughly reverse arrays and their order, dropping empty ones
    filtered_arrays = list(reversed([arr for arr in input_array if arr]))
    
    # Result tracking
    result = []
    seen = set()
    
    # Extremely precise multi-pass strategy
    for current_arr in filtered_arrays:
        # Reverse the current array
        reversed_current = list(reversed(current_arr))
        
        # Temporary storage for unique items
        temp_unique = []
        
        # Unique item tracking
        for item in reversed_current:
            if item not in seen:
                temp_unique.append(item)
                seen.add(item)
        
        # Critical: Prepend in specific order
        result = temp_unique + result
    
    return result