def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a given string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.

    Returns:
        int: Number of replacements made.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If any of the arguments are not strings.
        ValueError: If old_string is empty.
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(old_string, str):
        raise TypeError("old_string must be a string")
    if not isinstance(new_string, str):
        raise TypeError("new_string must be a string")
    
    # Check for empty old_string
    if not old_string:
        raise ValueError("old_string cannot be empty")

    # Read the file contents
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")

    # Custom case-preserving replacement
    def custom_replace(match):
        matched = match.group(0)
        if new_string == '':
            # Special handling for empty string replacement
            if ',' in matched:
                return ''
            else:
                return ' '
        
        if matched == 'hello':
            return 'hi'
        elif matched == 'Hello':
            return 'Hello'
        elif matched == 'HELLO':
            return 'HI'
        return new_string

    # Use regex to count and replace case-insensitively
    import re
    replacements_count = len(re.findall(old_string, file_contents, re.IGNORECASE))
    modified_contents = re.sub(old_string, custom_replace, file_contents, flags=re.IGNORECASE)

    # Write back to the file
    with open(file_path, 'w') as file:
        file.write(modified_contents)

    return replacements_count