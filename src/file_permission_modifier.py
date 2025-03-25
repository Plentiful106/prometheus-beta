import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions need to be modified.
        mode (int): The new permission mode (e.g., 0o755 for rwxr-xr-x).

    Returns:
        bool: True if permissions were successfully changed.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to modify the file.
        TypeError: If incorrect types are provided for arguments.
        ValueError: If an invalid permission mode is specified.
    """
    # Validate input types with more explicit type checking
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Normalize file path to handle potential relative paths
    file_path = os.path.abspath(os.path.expanduser(file_path))
    
    # Validate file existence with more robust checking
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist or is not a regular file")
    
    # More strict permission mode validation
    if not 0 <= mode <= 0o777:
        raise ValueError(f"Invalid permission mode {mode}. Must be between 0 and 0o777")
    
    try:
        # Attempt to change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    except OSError as e:
        raise OSError(f"Error changing file permissions: {e}")
    
    return True