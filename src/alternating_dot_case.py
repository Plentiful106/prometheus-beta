def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> convert_to_alternating_dot_case("hello world")
        'h.E.l.L.o. .W.o.R.l.D.'
        >>> convert_to_alternating_dot_case("Python")
        'P.y.T.h.O.n.'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert to alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # Alternate between lowercase and uppercase
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
        
        # Add dot after each character except the last
        if i < len(input_string) - 1:
            result.append('.')
    
    return ''.join(result)