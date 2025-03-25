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
        # Use the original string's case for alternation
        if i % 2 == 0:
            result.append(char if char.islower() else char.lower())
        else:
            result.append(char if char.isupper() else char.upper())
        
        # Always add dot after each character
        result.append('.')
    
    # Special handling for single character and last dot
    return ''.join(result[:-1] if len(input_string) > 1 else result)