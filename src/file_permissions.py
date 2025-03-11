import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions of a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing file permission details with keys:
            - 'numeric': Numeric representation of file permissions (e.g., 644)
            - 'symbolic': Symbolic representation of file permissions (e.g., 'rw-r--r--')
            - 'owner_read': Boolean indicating if owner has read permission
            - 'owner_write': Boolean indicating if owner has write permission
            - 'owner_execute': Boolean indicating if owner has execute permission
            - 'group_read': Boolean indicating if group has read permission
            - 'group_write': Boolean indicating if group has write permission
            - 'group_execute': Boolean indicating if group has execute permission
            - 'others_read': Boolean indicating if others have read permission
            - 'others_write': Boolean indicating if others have write permission
            - 'others_execute': Boolean indicating if others have execute permission

    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If there's no permission to access the file
    """
    try:
        # Get file stats
        file_stat = os.stat(file_path)
        
        # Get numeric permissions
        numeric_perms = oct(file_stat.st_mode)[-3:]
        
        # Convert numeric permissions to symbolic representation
        symbolic_perms = ''
        owner_perms = (file_stat.st_mode & stat.S_IRWXU) >> 6
        group_perms = (file_stat.st_mode & stat.S_IRWXG) >> 3
        others_perms = file_stat.st_mode & stat.S_IRWXO
        
        # Owner permissions
        symbolic_perms += 'r' if owner_perms & 4 else '-'
        symbolic_perms += 'w' if owner_perms & 2 else '-'
        symbolic_perms += 'x' if owner_perms & 1 else '-'
        
        # Group permissions
        symbolic_perms += 'r' if group_perms & 4 else '-'
        symbolic_perms += 'w' if group_perms & 2 else '-'
        symbolic_perms += 'x' if group_perms & 1 else '-'
        
        # Others permissions
        symbolic_perms += 'r' if others_perms & 4 else '-'
        symbolic_perms += 'w' if others_perms & 2 else '-'
        symbolic_perms += 'x' if others_perms & 1 else '-'
        
        return {
            'numeric': numeric_perms,
            'symbolic': symbolic_perms,
            'owner_read': bool(owner_perms & 4),
            'owner_write': bool(owner_perms & 2),
            'owner_execute': bool(owner_perms & 1),
            'group_read': bool(group_perms & 4),
            'group_write': bool(group_perms & 2),
            'group_execute': bool(group_perms & 1),
            'others_read': bool(others_perms & 4),
            'others_write': bool(others_perms & 2),
            'others_execute': bool(others_perms & 1)
        }
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"No permission to access the file {file_path}.")
    except Exception as e:
        raise OSError(f"Error retrieving file permissions: {str(e)}")