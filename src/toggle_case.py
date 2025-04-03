def toggle_case(input_string: str) -> str:
    """
    Convert all lowercase characters to uppercase and all uppercase characters to lowercase.

    Args:
        input_string (str): The input string to transform.

    Returns:
        str: A new string with letter cases toggled.

    Examples:
        >>> toggle_case('Hello, World!')
        'hELLO, wORLD!'
        >>> toggle_case('Python 3.9')
        'pYTHON 3.9'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.swapcase()