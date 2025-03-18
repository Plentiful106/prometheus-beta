import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_basic_string_replacement(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world, hello Universe")
    
    # Perform replacement
    replacements = replace_string_in_file(str(test_file), "hello", "hi")
    
    # Check results
    assert replacements == 2
    assert test_file.read_text() == "Hello world, hi Universe"

def test_no_replacements(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    original_content = "Hello world"
    test_file.write_text(original_content)
    
    # Perform replacement
    replacements = replace_string_in_file(str(test_file), "xyz", "abc")
    
    # Check results
    assert replacements == 0
    assert test_file.read_text() == original_content

def test_empty_new_string(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world, hello Universe")
    
    # Perform replacement
    replacements = replace_string_in_file(str(test_file), "hello", "")
    
    # Check results
    assert replacements == 2
    assert test_file.read_text() == "Hello world, Universe"

def test_file_not_found():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string(tmp_path):
    # Test empty old string
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world")
    
    with pytest.raises(ValueError):
        replace_string_in_file(str(test_file), "", "new")