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
    
    # Reverse each sub-array and reverse their order
    arrays = list(reversed([list(reversed(arr)) for arr in non_empty_arrays]))
    
    # Tracking unique values with a special order
    result = []
    seen = set()
    
    # Custom multi-pass strategy
    for arr in arrays:
        # Temporary storage for unique elements
        unique_temp = []
        
        # Collect unique elements
        for item in arr:
            if item not in seen:
                seen.add(item)
                unique_temp.append(item)
        
        # Critical: Insert at the beginning
        result = unique_temp + result
    
    return result