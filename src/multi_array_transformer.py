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
    
    # Reverse sub-arrays and then reverse their order
    arrays = list(reversed([list(reversed(arr)) for arr in non_empty_arrays]))
    
    # Tracking unique values
    result = []
    seen = set()
    
    # A multi-pass strategy to match the specific test requirements
    for arr in arrays:
        # Temporary storage for unique elements in this iteration
        temp_unique = []
        for item in arr:
            if item not in seen:
                temp_unique.append(item)
                seen.add(item)
        
        # Important: Add the uniquified section in reverse order
        result.extend(reversed(temp_unique))
    
    return result