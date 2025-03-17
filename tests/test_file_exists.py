import os
import pytest
from src.file_exists import is_file_exists

def test_existing_file(tmp_path):
    """Test that an existing file returns True."""
    test_file = tmp_path / "existing_file.txt"
    test_file.write_text("Test content")
    assert is_file_exists(str(test_file)) is True

def test_non_existing_file(tmp_path):
    """Test that a non-existing file returns False."""
    non_existing_file = tmp_path / "non_existing_file.txt"
    assert is_file_exists(str(non_existing_file)) is False

def test_directory(tmp_path):
    """Test that a directory returns False."""
    assert is_file_exists(str(tmp_path)) is False

def test_invalid_input_type():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        is_file_exists(123)
        is_file_exists(None)

def test_empty_string():
    """Test behavior with an empty string path."""
    assert is_file_exists("") is False

def test_whitespace_string():
    """Test behavior with whitespace string path."""
    assert is_file_exists("   ") is False