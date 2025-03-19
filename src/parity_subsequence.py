def longest_parity_subsequence(arr):
    """
    Find the longest subsequence with the same parity (all even or all odd) in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest subsequence with consistent parity
    
    Examples:
        >>> longest_parity_subsequence([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> longest_parity_subsequence([1, 3, 5, 7])
        [1, 3, 5, 7]
        >>> longest_parity_subsequence([])
        []
    """
    if not arr:
        return []
    
    # Try finding the longest even subsequence
    even_seq = [num for num in arr if num % 2 == 0]
    
    # Try finding the longest odd subsequence
    odd_seq = [num for num in arr if num % 2 != 0]
    
    # Return the longer subsequence, preferring odd if equal length
    return odd_seq if len(odd_seq) >= len(even_seq) else even_seq