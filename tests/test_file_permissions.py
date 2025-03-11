import os
import pytest
import stat
import tempfile
import sys

from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file():
    # Create a temporary file with specific permissions
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        os.chmod(temp_file.name, 0o644)  # rw-r--r--
        
        # Get file permissions
        perms = get_file_permissions(temp_file.name)
        
        # Check numeric permissions
        assert perms['numeric'] == '644'
        
        # Check symbolic permissions
        assert perms['symbolic'] == 'rw-r--r--'
        
        # Check individual permissions
        assert perms['owner_read'] is True
        assert perms['owner_write'] is True
        assert perms['owner_execute'] is False
        assert perms['group_read'] is True
        assert perms['group_write'] is False
        assert perms['group_execute'] is False
        assert perms['others_read'] is True
        assert perms['others_write'] is False
        assert perms['others_execute'] is False
        
        # Clean up
        os.unlink(temp_file.name)

def test_get_file_permissions_different_modes():
    test_cases = [
        (0o700, '700', 'rwx------'),
        (0o755, '755', 'rwxr-xr-x'),
        (0o777, '777', 'rwxrwxrwx'),
        (0o600, '600', 'rw-------'),
        (0o666, '666', 'rw-rw-rw-')
    ]
    
    for mode, numeric, symbolic in test_cases:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            os.chmod(temp_file.name, mode)
            
            perms = get_file_permissions(temp_file.name)
            
            assert perms['numeric'] == numeric
            assert perms['symbolic'] == symbolic
            
            os.unlink(temp_file.name)

def test_get_file_permissions_non_existent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions('/path/to/non/existent/file.txt')

def test_get_file_permissions_unreadable_file():
    if sys.platform == 'linux':
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            # Remove all permissions
            os.chmod(temp_file.name, 0o000)
            
            with pytest.raises(PermissionError):
                get_file_permissions(temp_file.name)
            
            os.unlink(temp_file.name)
    else:
        pytest.skip("This test requires a Linux-like environment")