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
    
    # Unique tracking
    result = []
    seen = set()
    
    # Specific multi-pass strategy
    for arr in reversed(non_empty_arrays):
        # Reverse current array
        reversed_arr = list(reversed(arr))
        
        # Temporary storage for unique elements
        unique_temp = []
        
        # Tracking unique elements
        for item in reversed_arr:
            if item not in seen:
                unique_temp.append(item)
                seen.add(item)
        
        # Prepend these unique items to the result
        result = unique_temp + result
    
    return result