def switch_cases(str1: str, str2: str) -> str:
    """
    Swap the character cases between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: A new string with characters from str1 and str2 with their cases swapped
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If the input strings have different lengths
    
    Examples:
        >>> switch_cases("Hello", "WORLD")
        "hELLO"
        >>> switch_cases("AbCdE", "12345")
        "aBcDe"
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Validate input lengths
    if len(str1) != len(str2):
        raise ValueError("Input strings must have equal length")
    
    # Swap cases
    return ''.join(
        c.lower() if c.isupper() else c.upper() 
        for c in str1
    )