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
    # First, reverse the input array and remove empty sub-arrays
    reversed_arrays = list(reversed([arr for arr in input_array if arr]))
    
    # Reverse each sub-array
    reversed_subarrays = [list(reversed(arr)) for arr in reversed_arrays]
    
    # Track unique values and their order of first occurrence
    result = []
    seen = set()
    
    # Special handler to track the first occurrence of unique values
    for subarray in reversed_subarrays:
        unique_subarray = []
        for item in subarray:
            if item not in seen:
                unique_subarray.append(item)
                seen.add(item)
        
        # Extend the result with these unique items
        result.extend(reversed(unique_subarray))
    
    return result