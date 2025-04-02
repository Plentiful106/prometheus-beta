import os
import pytest
import tempfile
from src.file_merger import merge_files

def test_merge_files_basic():
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f:
            f.write("Hello")
        with open(file2, 'w') as f:
            f.write("World")
        
        # Merge files
        merge_files([file1, file2], output)
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "Hello\n\nWorld"

def test_merge_files_custom_delimiter():
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f:
            f.write("Hello")
        with open(file2, 'w') as f:
            f.write("World")
        
        # Merge files with custom delimiter
        merge_files([file1, file2], output, delimiter=' | ')
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "Hello | World"

def test_merge_files_empty_list_error():
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        
        # Should raise ValueError for empty input list
        with pytest.raises(ValueError, match="input_files cannot be empty"):
            merge_files([], output)

def test_merge_files_nonexistent_file_error():
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        # Should raise FileNotFoundError for nonexistent file
        with pytest.raises(FileNotFoundError):
            merge_files([nonexistent_file], output)

def test_merge_files_invalid_input_types():
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        
        # Should raise TypeError for non-list input
        with pytest.raises(TypeError, match="input_files must be a list of file paths"):
            merge_files("not a list", output)
        
        # Should raise TypeError for list with non-string elements
        with pytest.raises(TypeError, match="All elements in input_files must be strings"):
            merge_files([1, 2, 3], output)

def test_merge_files_multiple_files():
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple input files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        file3 = os.path.join(tmpdir, 'file3.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f:
            f.write("First")
        with open(file2, 'w') as f:
            f.write("Second")
        with open(file3, 'w') as f:
            f.write("Third")
        
        # Merge files
        merge_files([file1, file2, file3], output)
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "First\n\nSecond\n\nThird"