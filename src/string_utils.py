def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a given string.

    Args:
        text (str): The input string to be transformed.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming language")
        'Python Programming Language'
        >>> capitalize_words("")
        ''
        >>> capitalize_words("a")
        'A'
    """
    # Handle empty string case
    if not text:
        return text
    
    # Split the string into words and capitalize the first letter of each
    return ' '.join(word.capitalize() for word in text.split())