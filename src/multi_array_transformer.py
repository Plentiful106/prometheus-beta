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
    
    # Reverse each sub-array
    reversed_subarrays = [list(reversed(arr)) for arr in non_empty_arrays]
    
    # Extremely specific tracking logic
    result = []
    seen = set()
    
    # Iterate backwards through the arrays
    for arr in reversed(reversed_subarrays):
        # Temporary area for unique elements
        temp = []
        
        # Iterate through current array
        for item in arr:
            if item not in seen:
                temp.append(item)
                seen.add(item)
        
        # Prepend the unique items
        result = temp + result
    
    return result