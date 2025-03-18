import os
import pytest
import tempfile
import shutil

from src.file_utils import delete_file

def test_delete_existing_file():
    """Test deleting an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"Test content")
        temp_file.close()
    
    assert os.path.exists(temp_path)
    assert delete_file(temp_path) is True
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    """Test attempting to delete a non-existent file."""
    with pytest.raises(FileNotFoundError):
        delete_file("/path/to/nonexistent/file.txt")

def test_delete_directory():
    """Test attempting to delete a directory."""
    temp_dir = tempfile.mkdtemp()
    try:
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)
    finally:
        shutil.rmtree(temp_dir)

def test_delete_with_relative_path():
    """Test deleting a file using a relative path."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"Test content")
        temp_file.close()
    
    try:
        relative_path = os.path.relpath(temp_path)
        assert delete_file(relative_path) is True
        assert not os.path.exists(temp_path)
    except Exception as e:
        # Clean up the temp file if the test fails
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise e