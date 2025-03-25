import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions need to be modified.
        mode (int): The new permission mode (e.g., 0o755 for rwxr-xr-x).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to modify the file.
        TypeError: If incorrect types are provided for arguments.
        ValueError: If an invalid permission mode is specified.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    # Validate permission mode (ensure it's a valid octal mode)
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid permission mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    except Exception as e:
        raise OSError(f"Error changing file permissions: {str(e)}")
    
    return True