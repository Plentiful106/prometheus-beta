def count_zero_sum_pairs(arr):
    """
    Count the number of pairs of elements in the input array that sum up to zero.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The number of pairs that sum to zero.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.

    Examples:
        >>> count_zero_sum_pairs([1, -1, 2, -2, 3])
        2
        >>> count_zero_sum_pairs([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if any(not isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Use a set for O(n) time complexity
    seen = set()
    zero_sum_pairs = 0
    
    for num in arr:
        # If the negative of the current number exists in seen, we found a pair
        if -num in seen:
            zero_sum_pairs += 1
        # Add current number to seen
        seen.add(num)
    
    return zero_sum_pairs