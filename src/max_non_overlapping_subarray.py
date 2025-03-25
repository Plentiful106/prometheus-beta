def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray in the given array.
    
    A non-overlapping subarray is a contiguous part of the array that does not 
    share any indices with another subarray in the maximum sum calculation.
    
    Args:
        arr (list): A list of integers to analyze.
    
    Returns:
        int: The maximum sum of non-overlapping subarrays.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty.
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([1, -1, 1, -1, 1])
        2
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # If array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Dynamic programming approach to find max non-overlapping subarray sum
    n = len(arr)
    
    # dp[i] represents the maximum sum of non-overlapping subarrays up to index i
    dp = [0] * n
    
    # Initialize first two elements
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1], arr[0] + arr[1])
    
    # Iterate through the array starting from index 2
    for i in range(2, n):
        # Two choices at each step:
        # 1. Include current element and the best sum two steps back
        # 2. Skip current element and use previous best sum
        dp[i] = max(arr[i], 
                    dp[i-1],  # don't include current element 
                    dp[i-2] + arr[i])  # include current element and best non-overlapping sum before it
    
    # Return the maximum sum
    return dp[-1]