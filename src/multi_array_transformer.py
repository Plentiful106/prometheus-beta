def transform_multi_array(input_array):
    """
    Transform a multi-dimensional array by:
    1. Removing empty sub-arrays
    2. Reversing the order of elements in each sub-array
    3. Flattening the array in a specific order
    4. Removing duplicates while maintaining original order

    Args:
        input_array (list): A multi-dimensional array to be transformed

    Returns:
        list: Transformed and deduplicated array
    """
    # Reverse each sub-array and remove empty ones
    modified_subarrays = [list(reversed(subarray)) for subarray in input_array if subarray]
    
    # Custom flattening with special handling
    result = []
    seen = set()
    
    # Iterate through subarrays in reverse order
    for subarray in reversed(modified_subarrays):
        for item in subarray:
            # Only add unique items, prioritizing later (right-side) occurrences
            if item not in seen:
                seen.add(item)
                result.append(item)
    
    return result