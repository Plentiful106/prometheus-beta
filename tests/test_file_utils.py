import os
import pytest
import shutil
from src.file_utils import rename_file

@pytest.fixture
def temp_files(tmp_path):
    """Create temporary test files and directories."""
    # Create a test directory
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Create a source file
    source_file = test_dir / "source.txt"
    source_file.write_text("Test content")

    return {
        'test_dir': test_dir,
        'source_file': str(source_file)
    }

def test_rename_file_success(temp_files):
    """Test successful file renaming."""
    source_path = temp_files['source_file']
    dest_path = os.path.join(os.path.dirname(source_path), "destination.txt")
    
    result = rename_file(source_path, dest_path)
    
    assert result == dest_path
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_to_different_directory(temp_files):
    """Test renaming a file to a different directory."""
    source_path = temp_files['source_file']
    dest_dir = os.path.join(os.path.dirname(source_path), "new_dir")
    dest_path = os.path.join(dest_dir, "destination.txt")
    
    result = rename_file(source_path, dest_path)
    
    assert result == dest_path
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_file_not_found():
    """Test renaming a non-existent file."""
    with pytest.raises(FileNotFoundError):
        rename_file("non_existent_file.txt", "new_file.txt")

def test_rename_to_existing_file(temp_files):
    """Test attempting to rename to an existing file."""
    source_path = temp_files['source_file']
    existing_file = os.path.join(os.path.dirname(source_path), "existing.txt")
    
    # Create existing file
    with open(existing_file, 'w') as f:
        f.write("Existing content")
    
    with pytest.raises(FileExistsError):
        rename_file(source_path, existing_file)

def test_rename_directory_raises_error(temp_files):
    """Test attempting to rename a directory."""
    source_dir = os.path.dirname(temp_files['source_file'])
    dest_path = os.path.join(os.path.dirname(source_dir), "new_dir")
    
    with pytest.raises(IsADirectoryError):
        rename_file(source_dir, dest_path)

def test_rename_invalid_input_type():
    """Test renaming with invalid input types."""
    with pytest.raises(TypeError):
        rename_file(123, "new_file.txt")
    with pytest.raises(TypeError):
        rename_file("source.txt", 456)