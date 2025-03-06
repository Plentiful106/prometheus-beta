"""
Tests for file writing utility function.
"""
import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_success():
    """Test writing a string to a file successfully."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test_file.txt')
        test_content = "Hello, world!"
        
        write_string_to_file(test_file, test_content)
        
        with open(test_file, 'r') as file:
            assert file.read() == test_content

def test_write_string_to_file_overwrite():
    """Test that writing to an existing file overwrites its content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test_file.txt')
        
        # First write
        write_string_to_file(test_file, "First content")
        
        # Overwrite
        write_string_to_file(test_file, "Updated content")
        
        with open(test_file, 'r') as file:
            assert file.read() == "Updated content"

def test_write_string_to_file_unicode():
    """Test writing unicode characters."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'unicode_file.txt')
        test_content = "こんにちは世界"  # Hello world in Japanese
        
        write_string_to_file(test_file, test_content)
        
        with open(test_file, 'r', encoding='utf-8') as file:
            assert file.read() == test_content

def test_write_string_to_file_invalid_path_type():
    """Test raising TypeError for invalid path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for invalid content type."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("file.txt", 123)

def test_write_string_to_file_empty_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")