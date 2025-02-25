import os
from typing import Optional, Union


def find_oldest_file(directory: Union[str, os.PathLike]) -> Optional[str]:
    """
    Find the oldest file in a given directory.

    Args:
        directory (str or os.PathLike): Path to the directory to search.

    Returns:
        Optional[str]: Path to the oldest file, or None if the directory is empty or invalid.

    Raises:
        TypeError: If the directory is not a string or path-like object.
        NotADirectoryError: If the provided path is not a directory.
    """
    # Validate input
    if not isinstance(directory, (str, os.PathLike)):
        raise TypeError("Directory must be a string or path-like object")

    # Convert to absolute path and check if it's a directory
    directory = os.path.abspath(directory)
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory")

    # List all files in the directory (excluding directories)
    try:
        files = [
            os.path.join(directory, f) 
            for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f))
        ]

        # If no files, return None
        if not files:
            return None

        # Find the oldest file based on creation time
        oldest_file = min(files, key=os.path.getctime)
        return oldest_file

    except PermissionError:
        # Handle cases where directory cannot be accessed
        return None
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"Error searching for oldest file: {str(e)}")