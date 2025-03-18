import os
import pytest
import tempfile
import shutil

from src.file_counter import count_files_in_directory

def test_count_files_in_empty_directory():
    """Test counting files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_count_files_in_directory_with_files():
    """Test counting files in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        for i in range(5):
            open(os.path.join(temp_dir, f'file{i}.txt'), 'w').close()
        
        assert count_files_in_directory(temp_dir) == 5

def test_count_files_ignores_subdirectories():
    """Test that subdirectories are not counted as files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files
        for i in range(3):
            open(os.path.join(temp_dir, f'file{i}.txt'), 'w').close()
        
        # Create a subdirectory
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        os.mkdir(os.path.join(temp_dir, 'another_subdir'))
        
        assert count_files_in_directory(temp_dir) == 3

def test_nonexistent_directory():
    """Test that a FileNotFoundError is raised for a non-existent directory."""
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_file_as_directory():
    """Test that a NotADirectoryError is raised when a file is passed."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)

def test_hidden_files():
    """Test that hidden files are counted."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some hidden files
        for i in range(3):
            open(os.path.join(temp_dir, f'.hidden{i}.txt'), 'w').close()
        
        assert count_files_in_directory(temp_dir) == 3