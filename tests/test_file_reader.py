import os
import pytest
from src.file_reader import read_file_contents

def test_read_file_contents_success(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, this is a test file!"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_file_contents_non_existent_file():
    # Test reading a non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_read_file_contents_empty_file(tmp_path):
    # Create an empty file and verify it returns an empty string
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    result = read_file_contents(str(test_file))
    assert result == ""