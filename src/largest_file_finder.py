import os
from typing import Union, Optional

def find_largest_file(directory: str) -> Optional[str]:
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search for the largest file.

    Returns:
        Optional[str]: Path to the largest file, or None if no files exist or directory is invalid.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    # Validate input
    if not os.path.exists(directory):
        return None
    
    if not os.path.isdir(directory):
        raise ValueError(f"Provided path '{directory}' is not a directory")
    
    largest_file = None
    largest_size = 0
    
    # Walk through the directory
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip if not a file or cannot be accessed
                if not os.path.isfile(file_path):
                    continue
                
                try:
                    # Attempt to read the file size without reading contents
                    file_size = os.path.getsize(file_path)
                    
                    # Attempt to verify file is readable (without fully reading)
                    try:
                        with open(file_path, 'rb') as f:
                            f.seek(0, 2)  # Seek to end of file
                            readable_size = f.tell()  # Check if readable
                    except (PermissionError, IOError):
                        continue
                    
                    # Update largest file if current file is larger and fully readable
                    if file_size > largest_size and readable_size == file_size:
                        largest_file = file_path
                        largest_size = file_size
                except (OSError, PermissionError):
                    # Skip files that can't be accessed
                    continue
    
    except PermissionError:
        # Handle cases where directory cannot be accessed
        return None
    
    return largest_file