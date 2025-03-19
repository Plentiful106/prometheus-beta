def check_arithmetic_progression(arr):
    """
    Determine if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence of numbers where the difference 
    between consecutive terms is constant.
    
    Args:
        arr (list): A list of positive integers
    
    Returns:
        bool: True if any three consecutive numbers form an arithmetic progression, 
              False otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input contains non-positive integers
    
    Examples:
        >>> check_arithmetic_progression([2, 4, 6, 8, 10])  # True (2,4,6 or 4,6,8 or 6,8,10)
        True
        >>> check_arithmetic_progression([1, 2, 4, 8, 16])  # False
        False
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for minimum length
    if len(arr) < 3:
        return False
    
    # Validate all elements are positive integers
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # Check for arithmetic progression in consecutive triplets
    for i in range(len(arr) - 2):
        # Check if the difference between first two numbers equals 
        # the difference between the last two numbers
        if arr[i+1] - arr[i] == arr[i+2] - arr[i+1]:
            return True
    
    return False