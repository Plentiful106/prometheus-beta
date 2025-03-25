import os
import stat
import pathlib

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file securely and comprehensively.

    Args:
        file_path (str): Absolute or relative path to the file to modify.
        mode (int): Octal permission mode (e.g., 0o755).

    Returns:
        bool: True if file permissions were successfully changed.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If insufficient permissions to modify the file.
        TypeError: If input types are incorrect.
        ValueError: If permission mode is invalid.
    """
    # Type validation with strict checking
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("Permission mode must be an integer")
    
    # Resolve and normalize path
    try:
        resolved_path = str(pathlib.Path(file_path).resolve())
    except Exception as e:
        raise ValueError(f"Invalid file path: {e}")
    
    # Comprehensive file existence check
    if not os.path.exists(resolved_path):
        raise FileNotFoundError(f"File not found: {resolved_path}")
    
    if not os.path.isfile(resolved_path):
        raise ValueError(f"Path is not a file: {resolved_path}")
    
    # Strict permission mode validation
    if mode < 0 or mode > 0o777:
        raise ValueError(f"Invalid permission mode: {mode}. Must be between 0 and 0o777")
    
    try:
        # Attempt file permission modification
        os.chmod(resolved_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify file: {resolved_path}")
    except OSError as e:
        raise OSError(f"Failed to change file permissions: {e}")
    
    return True