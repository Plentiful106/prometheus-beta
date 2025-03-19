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
    # Remove empty sub-arrays and reverse each sub-array
    modified_arrays = [list(reversed(arr)) for arr in input_array if arr]
    
    # Reverse the order of sub-arrays
    modified_arrays = list(reversed(modified_arrays))
    
    # Using a specific strategy to extract unique values
    seen = set()
    result = []
    
    # Iterate through sub-arrays
    for arr in modified_arrays:
        # Create a temporary list for unique items in this sub-array
        unique_items = []
        for item in arr:
            if item not in seen:
                unique_items.append(item)
                seen.add(item)
        
        # Add unique items at the end of the result list
        result.extend(unique_items)
    
    return result