def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.

    Args:
        n (int): The input integer to count set bits in.

    Returns:
        int: The number of set bits in the binary representation of the input.

    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> count_set_bits(5)  # Binary: 101
        2
        >>> count_set_bits(0)
        0
        >>> count_set_bits(-5)  # Two's complement representation
        2
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to positive 
    # using bitwise AND with a signed integer's maximum value
    n = abs(n)
    
    # Count set bits
    count = 0
    while n:
        # Check least significant bit and increment count if it's 1
        count += n & 1
        # Right shift to check next bit
        n >>= 1
    
    return count