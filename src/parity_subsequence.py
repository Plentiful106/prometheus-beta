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
    
    # Separate even and odd numbers while preserving order
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    # If no numbers of a particular parity, return other parity
    if not even_numbers:
        return odd_numbers
    if not odd_numbers:
        return even_numbers
    
    # Preferring the subsequence that appears first in the original array
    if arr.index(even_numbers[0]) <= arr.index(odd_numbers[0]):
        return even_numbers if len(even_numbers) >= len(odd_numbers) else odd_numbers
    else:
        return odd_numbers if len(odd_numbers) >= len(even_numbers) else even_numbers