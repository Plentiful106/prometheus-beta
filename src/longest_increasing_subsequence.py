def longest_increasing_subsequence(arr):
    """
    Calculate the length of the longest increasing subsequence in an array.
    
    A subsequence is a sequence that can be derived from an array by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        - [10, 22, 9, 33, 21, 50, 41, 60, 80] returns 6
        - [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] returns 6
        - [] returns 0
        - [5] returns 1
    """
    # Handle edge cases
    if not arr:
        return 0
    
    # Initialize DP array to store lengths of increasing subsequences
    n = len(arr)
    dp = [1] * n
    
    # Dynamic programming approach to find longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)