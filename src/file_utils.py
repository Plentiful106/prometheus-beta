import os

def delete_file(file_path):
    """
    Delete a file from the specified path.

    Args:
        file_path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
        OSError: For other OS-related errors during file deletion.

    Returns:
        bool: True if the file was successfully deleted.
    """
    # Normalize the path to handle potential relative paths
    normalized_path = os.path.abspath(os.path.expanduser(file_path))

    # Check if the path exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Ensure it's a file, not a directory
    if os.path.isdir(normalized_path):
        raise IsADirectoryError(f"The path {file_path} is a directory, not a file.")

    # Attempt to delete the file
    try:
        os.remove(normalized_path)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to delete {file_path}")
    except OSError as e:
        raise OSError(f"Error deleting {file_path}: {str(e)}")