def convert_to_pascal_case(input_string: str) -> str:
    """
    Convert a given string to Pascal case.
    
    Pascal case is a naming convention where the first letter of each word is capitalized,
    and there are no separators between words.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_pascal_case("hello world")
        'HelloWorld'
        >>> convert_to_pascal_case("python_programming_language")
        'PythonProgrammingLanguage'
        >>> convert_to_pascal_case("snake_case_example")
        'SnakeCaseExample'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove any leading/trailing whitespace
    input_string = input_string.strip()
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string by non-alphanumeric characters
    words = ''.join(char if char.isalnum() else ' ' for char in input_string).split()
    
    # Capitalize first letter of each word and join
    return ''.join(word.capitalize() for word in words)