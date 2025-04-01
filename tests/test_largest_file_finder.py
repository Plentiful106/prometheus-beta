import os
import pytest
import tempfile
import shutil

from src.largest_file_finder import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a simple directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different sizes
        with open(os.path.join(temp_dir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(temp_dir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        largest_file = find_largest_file(temp_dir)
        assert largest_file is not None
        assert os.path.basename(largest_file) == 'large.txt'

def test_find_largest_file_nested():
    """Test finding the largest file in a nested directory structure"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directories with files
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        
        with open(os.path.join(temp_dir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(temp_dir, 'subdir1', 'medium.txt'), 'w') as f:
            f.write('medium' * 50)
        
        with open(os.path.join(temp_dir, 'subdir2', 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        largest_file = find_largest_file(temp_dir)
        assert largest_file is not None
        assert os.path.basename(largest_file) == 'large.txt'

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        largest_file = find_largest_file(temp_dir)
        assert largest_file is None

def test_find_largest_file_nonexistent_directory():
    """Test behavior with a non-existent directory"""
    with tempfile.TemporaryDirectory() as parent_dir:
        nonexistent_dir = os.path.join(parent_dir, 'nonexistent')
        largest_file = find_largest_file(nonexistent_dir)
        assert largest_file is None

def test_find_largest_file_invalid_directory():
    """Test error handling for non-directory path"""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(ValueError):
            find_largest_file(test_file)

def test_find_largest_file_file_permissions(monkeypatch):
    """Test handling of files with restricted permissions"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        with open(os.path.join(temp_dir, 'readable.txt'), 'w') as f:
            f.write('readable' * 10)
        
        # Create a file with no read permissions
        no_read_file = os.path.join(temp_dir, 'no_read.txt')
        with open(no_read_file, 'w') as f:
            f.write('no_read' * 100)
        os.chmod(no_read_file, 0o000)  # Remove all permissions
        
        try:
            largest_file = find_largest_file(temp_dir)
            assert largest_file is not None
            assert os.path.basename(largest_file) == 'readable.txt'
        finally:
            # Restore permissions to allow cleanup
            os.chmod(no_read_file, 0o666)