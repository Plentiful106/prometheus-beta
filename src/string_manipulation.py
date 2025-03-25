def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotate a string a specified number of times and then reverse it.
    
    Args:
        string (str): The input string to be rotated and reversed.
        rotations (int): Number of times to rotate the string.
    
    Returns:
        str: The rotated and reversed string.
    
    Raises:
        TypeError: If input is not a string or rotations is not an integer.
        ValueError: If rotations is negative.
    
    Examples:
        >>> rotate_and_reverse('hello', 2)
        'ohell'
        >>> rotate_and_reverse('python', 1)
        'npytho'
    """
    # Type checking
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    if not isinstance(rotations, int):
        raise TypeError("Rotations must be an integer")
    
    # Negative rotation check
    if rotations < 0:
        raise ValueError("Rotations cannot be negative")
    
    # Handle empty string or zero rotations
    if not string or rotations == 0:
        return string[::-1]
    
    # Normalize rotations to be within string length
    rotations = rotations % len(string)
    
    # Rotate and reverse
    rotated = string[rotations:] + string[:rotations]
    return rotated[::-1]