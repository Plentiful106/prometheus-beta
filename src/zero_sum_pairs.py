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
        >>> count_zero_sum_pairs([0, 0, 0])
        1
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if any(not isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Handle edge case of empty list or lists with insufficient elements
    if len(arr) < 2:
        return 0
    
    # Use a dictionary to count occurrences and track pairs
    count_dict = {}
    zero_sum_pairs = 0
    zero_count = 0
    
    for num in arr:
        # Count zeros separately
        if num == 0:
            zero_count += 1
            continue
        
        # If the negative of current number exists, we found a pair
        if -num in count_dict:
            zero_sum_pairs += 1
        
        # Increment count of current number
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Special handling for zeros
    if zero_count >= 2:
        zero_sum_pairs += 1
    
    return zero_sum_pairs