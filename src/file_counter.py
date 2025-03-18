import os
from typing import Union, List

def count_files_in_directory(directory_path: str) -> int:
    """
    Count the number of files directly in a given directory.

    This function counts only files, not subdirectories, and handles
    various edge cases like permission errors and non-existent paths.

    Args:
        directory_path (str): Path to the directory to count files in.

    Returns:
        int: Total number of files in the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Normalize the path to handle potential trailing slashes or relative paths
    directory_path = os.path.abspath(os.path.normpath(directory_path))

    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Specified path is not a directory: {directory_path}")
    
    try:
        # Use a more explicit comprehension to count files
        files = [
            f for f in os.listdir(directory_path) 
            if os.path.isfile(os.path.join(directory_path, f))
        ]
        return len(files)
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing directory: {directory_path}")
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"Unexpected error counting files: {e}")