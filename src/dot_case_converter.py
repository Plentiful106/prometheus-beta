def to_dot_case(input_string):
    """
    Convert a given string to dot case.
    
    Dot case is a string formatting where words are separated by dots,
    and all characters are lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_dot_case("HelloWorld")
        'hello.world'
        >>> to_dot_case("hello_world")
        'hello.world'
        >>> to_dot_case("Hello World")
        'hello.world'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace various separators with a temporary marker
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string into words, convert to lowercase
    words = normalized.split()
    
    # Join words with dots
    return '.'.join(word.lower() for word in words)