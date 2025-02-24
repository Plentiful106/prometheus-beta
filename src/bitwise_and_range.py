def bitwise_and_range(start: int, end: int) -> int:
    """
    Compute the bitwise AND of all numbers in the given range (inclusive).
    
    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).
    
    Returns:
        int: The result of bitwise AND operation across all numbers in the range.
    
    Raises:
        ValueError: If start is greater than end or if either number is negative.
    
    Examples:
        >>> bitwise_and_range(5, 7)  # 5 & 6 & 7
        4
        >>> bitwise_and_range(10, 10)  # Single number
        10
    """
    # Validate input
    if start < 0 or end < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # If range is single number, return that number
    if start == end:
        return start
    
    # Compute bitwise AND
    result = start
    for num in range(start + 1, end + 1):
        result &= num
    
    return result