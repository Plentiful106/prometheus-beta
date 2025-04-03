def find_longest_increasing_subsequence(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        int: The length of the longest increasing subsequence.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> find_longest_increasing_subsequence([])
        0
        >>> find_longest_increasing_subsequence([1])
        1
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return 0
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Dynamic Programming solution
    # Initialize DP array with 1s (each element is a subsequence of length 1)
    lis = [1] * len(arr)
    
    # Compute longest increasing subsequence
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Return the maximum length
    return max(lis)