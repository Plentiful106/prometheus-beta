def convert_to_upper_with_spaces(input_string):
    """
    Convert a string to uppercase, preserving existing spaces and adding spaces between words.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The converted string in uppercase with spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Remove extra whitespace and split into words
    words = input_string.strip().split()
    
    # Join words with a single space and convert to uppercase
    return " ".join(words).upper()