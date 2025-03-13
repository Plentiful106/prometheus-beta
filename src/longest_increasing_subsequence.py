def find_lis_length(nums):
    """
    Find the length of the Longest Increasing Subsequence (LIS) in a given list of numbers.
    
    Args:
        nums (list): A list of integers to find the LIS length for.
    
    Returns:
        int: Length of the longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-numeric elements.
    
    Examples:
        >>> find_lis_length([10, 22, 9, 33, 21, 50, 41, 60])
        5
        >>> find_lis_length([])
        0
        >>> find_lis_length([1])
        1
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Handle edge cases
    if not nums:
        return 0
    
    # Ensure all elements are numeric
    try:
        nums = [float(x) for x in nums]
    except (TypeError, ValueError):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution for LIS
    # dp[i] stores the length of the longest increasing subsequence ending at index i
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)