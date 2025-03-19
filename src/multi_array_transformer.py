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
    # Exact steps for transformation
    # Remove empty sub-arrays and reverse their contents
    non_empty_arrays = [list(reversed(arr)) for arr in input_array if arr]
    
    # Reverse the order of these arrays
    non_empty_arrays = list(reversed(non_empty_arrays))
    
    # Placeholder for result and tracking
    result = []
    seen = set()
    
    # Precisely tracking unique items
    for arr in non_empty_arrays:
        # Unique collection for this pass
        unique_temp = []
        
        # Tracking unique elements
        for item in arr:
            if item not in seen:
                unique_temp.append(item)
                seen.add(item)
        
        # Critical: Prepend unique items to result
        result = unique_temp + result
    
    return result