import os
import pytest
import time
import tempfile
import shutil


from src.oldest_file import find_oldest_file


def test_find_oldest_file_basic():
    """Test finding the oldest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with different creation times
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        
        # Create first file
        with open(file1, 'w') as f:
            f.write('test1')
        
        # Wait a bit to ensure different creation times
        time.sleep(1)
        
        # Create second file
        with open(file2, 'w') as f:
            f.write('test2')
        
        # Find the oldest file
        oldest = find_oldest_file(tmpdir)
        
        # Assert the first file is the oldest
        assert oldest == file1


def test_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Should return None for empty directory
        assert find_oldest_file(tmpdir) is None


def test_invalid_directory():
    """Test error handling for invalid directory."""
    with pytest.raises(NotADirectoryError):
        find_oldest_file('/non/existent/directory/path')


def test_invalid_input_type():
    """Test error handling for invalid input type."""
    with pytest.raises(TypeError):
        find_oldest_file(123)  # Non-string input


def test_permission_restricted_directory():
    """Test behavior with a directory that cannot be accessed."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a subdirectory with no read permissions
        restricted_dir = os.path.join(tmpdir, 'restricted')
        os.mkdir(restricted_dir)
        os.chmod(restricted_dir, 0o000)  # Remove all permissions
        
        try:
            # Should return None or not raise an exception
            result = find_oldest_file(restricted_dir)
            assert result is None
        finally:
            # Restore permissions to allow cleanup
            os.chmod(restricted_dir, 0o755)


def test_multiple_files_same_time():
    """Test handling multiple files created at the same time."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files
        files = [os.path.join(tmpdir, f'file{i}.txt') for i in range(3)]
        
        for f in files:
            with open(f, 'w') as file:
                file.write(f'test{f}')
        
        # Find the oldest file
        oldest = find_oldest_file(tmpdir)
        
        # Should return a valid file path
        assert oldest in files
        assert os.path.isfile(oldest)