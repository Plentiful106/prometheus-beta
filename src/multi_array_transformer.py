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
    
    # Track unique values in a specific way
    result = []
    seen = set()
    
    # Traverse in reversed order with special transformation
    for i in range(len(non_empty_arrays) - 1, -1, -1):
        # Reverse current array
        current_arr = list(reversed(non_empty_arrays[i]))
        
        # Handle unique values
        temp_unique = []
        for item in current_arr:
            if item not in seen:
                temp_unique.append(item)
                seen.add(item)
        
        # Prepend the unique items
        result = temp_unique + result
    
    return result