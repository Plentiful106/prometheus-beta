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
    
    # Find longest even and odd subsequences
    def get_longest_subsequence(predicate):
        longest = []
        current = []
        for num in arr:
            if predicate(num):
                current.append(num)
                if len(current) > len(longest):
                    longest = current.copy()
            else:
                current = []
        return longest
    
    even_subsequence = get_longest_subsequence(lambda x: x % 2 == 0)
    odd_subsequence = get_longest_subsequence(lambda x: x % 2 != 0)
    
    # Return the longer subsequence, preferring even if equal
    return max([even_subsequence, odd_subsequence], key=len)