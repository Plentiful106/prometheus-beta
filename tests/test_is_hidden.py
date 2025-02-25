import os
import pytest
import tempfile
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from is_hidden import is_hidden_file

def test_hidden_file_unix_style():
    """Test hidden file detection for Unix-like systems (dot prefix)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a hidden file
        hidden_file_path = os.path.join(tmpdir, '.hidden_test_file.txt')
        open(hidden_file_path, 'w').close()
        assert is_hidden_file(hidden_file_path) == True

def test_non_hidden_file():
    """Test non-hidden file detection."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a non-hidden file
        visible_file_path = os.path.join(tmpdir, 'visible_test_file.txt')
        open(visible_file_path, 'w').close()
        assert is_hidden_file(visible_file_path) == False

def test_invalid_input_type():
    """Test error handling for invalid input type."""
    with pytest.raises(TypeError):
        is_hidden_file(123)

def test_non_existent_file():
    """Test error handling for non-existent file."""
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/non/existent/file.txt')

def test_empty_string_path():
    """Test handling of empty string path."""
    with pytest.raises(FileNotFoundError):
        is_hidden_file('')