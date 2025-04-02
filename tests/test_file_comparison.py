"""
Unit tests for file comparison function.
"""

import os
import pytest
import tempfile
import shutil

from src.file_comparison import are_files_identical


def test_identical_files():
    """Test that identical files return True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two identical files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            test_content = "Hello, world!\nThis is a test file."
            f1.write(test_content)
            f2.write(test_content)
        
        assert are_files_identical(file1_path, file2_path) == True


def test_different_files():
    """Test that different files return False."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two different files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write("Content 1")
            f2.write("Content 2")
        
        assert are_files_identical(file1_path, file2_path) == False


def test_empty_files():
    """Test comparison of two empty files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two empty files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        open(file1_path, 'w').close()
        open(file2_path, 'w').close()
        
        assert are_files_identical(file1_path, file2_path) == True


def test_nonexistent_file():
    """Test that FileNotFoundError is raised for nonexistent files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        existing_file = os.path.join(temp_dir, 'existing.txt')
        with open(existing_file, 'w') as f:
            f.write("Content")
        
        # Test nonexistent first file
        with pytest.raises(FileNotFoundError):
            are_files_identical('/path/to/nonexistent/file1.txt', existing_file)
        
        # Test nonexistent second file
        with pytest.raises(FileNotFoundError):
            are_files_identical(existing_file, '/path/to/nonexistent/file2.txt')


def test_large_files():
    """Test comparison of large files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two large files
        file1_path = os.path.join(temp_dir, 'large1.txt')
        file2_path = os.path.join(temp_dir, 'large2.txt')
        
        # Create a 1MB file
        with open(file1_path, 'wb') as f1, open(file2_path, 'wb') as f2:
            f1.write(b'0' * (1024 * 1024))  # 1MB of zeros
            f2.write(b'0' * (1024 * 1024))  # 1MB of zeros
        
        assert are_files_identical(file1_path, file2_path) == True