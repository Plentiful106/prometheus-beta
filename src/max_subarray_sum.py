def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray of length k in the given array.

    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a contiguous subarray of length k

    Raises:
        ValueError: If k is invalid (less than or equal to 0 or greater than array length)
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check for invalid k values
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Edge case for empty array
    if not arr:
        return 0
    
    # Sliding window approach
    # Initially calculate the sum of first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max_sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum