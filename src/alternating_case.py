def convert_to_alternating_lower_case(input_string):
    """
    Convert a string to alternating lower case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with alternating lower case characters.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_alternating_lower_case("Hello World")
        'hElLo wOrLd'
        >>> convert_to_alternating_lower_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to alternating case
    return ''.join(
        char.lower() if idx % 2 == 0 else char.upper() 
        for idx, char in enumerate(input_string)
    )