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
    
    # Function to find the longest consecutive subsequence
    def find_longest_subsequence(pred):
        longest = []
        current = []
        
        for num in arr:
            if pred(num):
                current.append(num)
                if len(current) > len(longest):
                    longest = current[:]
            else:
                current = []
        
        return longest
    
    # Find longest consecutive even and odd subsequences
    even_subsequence = find_longest_subsequence(lambda x: x % 2 == 0)
    odd_subsequence = find_longest_subsequence(lambda x: x % 2 != 0)
    
    # Prefer the subsequence with more elements, breaking ties with even
    return max([even_subsequence, odd_subsequence], key=len)