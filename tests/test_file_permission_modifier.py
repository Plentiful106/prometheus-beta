import os
import pytest
import stat
import tempfile

from src.file_permission_modifier import change_file_permissions

def test_change_file_permissions_success():
    """Test successful file permission change."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
    # Initial permissions check
    initial_mode = os.stat(temp_path).st_mode
    
    # Change permissions
    result = change_file_permissions(temp_path, 0o755)
    
    # Verify changes
    assert result is True
    new_mode = os.stat(temp_path).st_mode
    assert stat.S_IMODE(new_mode) == 0o755
    
    # Clean up
    os.unlink(temp_path)

def test_change_file_permissions_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        change_file_permissions('/path/to/nonexistent/file.txt', 0o644)

def test_change_file_permissions_invalid_mode():
    """Test handling of invalid permission modes."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test negative mode
    with pytest.raises(ValueError):
        change_file_permissions(temp_path, -1)
    
    # Test mode greater than max octal
    with pytest.raises(ValueError):
        change_file_permissions(temp_path, 0o1000)
    
    # Clean up
    os.unlink(temp_path)

def test_change_file_permissions_invalid_input_types():
    """Test handling of incorrect input types."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test non-string file path
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o644)
    
    # Test non-integer mode
    with pytest.raises(TypeError):
        change_file_permissions(temp_path, '644')
    
    # Clean up
    os.unlink(temp_path)

def test_different_permission_modes():
    """Test changing to different permission modes."""
    modes_to_test = [0o444, 0o666, 0o777, 0o600]
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    for mode in modes_to_test:
        change_file_permissions(temp_path, mode)
        new_mode = os.stat(temp_path).st_mode
        assert stat.S_IMODE(new_mode) == mode
    
    # Clean up
    os.unlink(temp_path)