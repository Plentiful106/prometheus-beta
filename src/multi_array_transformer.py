def transform_multi_array(input_array):
    """
    Transform a multi-dimensional array by:
    1. Removing empty sub-arrays
    2. Reversing the order of elements in each sub-array
    3. Flattening the array in reverse order of input
    4. Removing duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional array to be transformed

    Returns:
        list: Transformed and deduplicated array
    """
    # Remove empty sub-arrays and reverse each sub-array
    reversed_arrays = [list(reversed(subarray)) for subarray in input_array if subarray]
    
    # Reverse the order of sub-arrays before flattening
    reversed_arrays = list(reversed(reversed_arrays))
    
    # Flatten the array
    flattened_array = [item for subarray in reversed_arrays for item in subarray]
    
    # Remove duplicates while maintaining order
    seen = set()
    deduplicated_array = []
    for item in flattened_array:
        if item not in seen:
            seen.add(item)
            deduplicated_array.append(item)
    
    return deduplicated_array