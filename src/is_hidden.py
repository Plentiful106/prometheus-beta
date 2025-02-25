import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden.

    Args:
        file_path (str): Path to the file to check for hidden status.

    Returns:
        bool: True if the file is hidden, False otherwise.

    Raises:
        TypeError: If file_path is not a string.
        FileNotFoundError: If the file does not exist or path is empty.
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    # Handle empty string path
    if not file_path:
        raise FileNotFoundError("Empty file path provided")

    # Normalize the path
    file_path = os.path.normpath(file_path)

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get the filename
    filename = os.path.basename(file_path)

    # Check hidden status based on platform
    if os.name == 'nt':  # Windows
        import ctypes
        FILE_ATTRIBUTE_HIDDEN = 0x02
        attributes = ctypes.windll.kernel32.GetFileAttributesA(file_path.encode())
        return attributes != -1 and bool(attributes & FILE_ATTRIBUTE_HIDDEN)
    else:  # Unix-like systems (Linux, macOS)
        # Hidden files start with a dot
        return filename.startswith('.')