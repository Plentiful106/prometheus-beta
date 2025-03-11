import os
import pytest
import tempfile
import shutil

from src.file_chunker import split_file_into_chunks, _parse_size_string

def test_parse_size_string():
    """Test parsing of size strings to bytes."""
    assert _parse_size_string('1KB') == 1024
    assert _parse_size_string('1MB') == 1024 * 1024
    assert _parse_size_string('1GB') == 1024 * 1024 * 1024
    assert _parse_size_string('500') == 500
    assert _parse_size_string('500B') == 500

    with pytest.raises(ValueError):
        _parse_size_string('invalid')
    with pytest.raises(ValueError):
        _parse_size_string('1XB')

def test_file_chunking_basic():
    """Test basic file chunking functionality."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b'0' * (1024 * 1024 * 2))  # 2MB file
        temp_source_path = temp_source.name

    try:
        # Create a temporary directory for output
        temp_output_dir = tempfile.mkdtemp()

        # Split the file
        chunks = split_file_into_chunks(
            temp_source_path, 
            chunk_size='1MB', 
            output_dir=temp_output_dir
        )

        # Verify chunks
        assert len(chunks) == 2
        assert all(os.path.exists(chunk) for chunk in chunks)
        
        # Verify chunk sizes
        chunk_sizes = [os.path.getsize(chunk) for chunk in chunks]
        assert chunk_sizes == [1024 * 1024, 1024 * 1024]

    finally:
        # Clean up
        os.unlink(temp_source_path)
        shutil.rmtree(temp_output_dir)

def test_file_chunking_small_file():
    """Test chunking a small file."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b'0' * 100)  # 100 bytes
        temp_source_path = temp_source.name

    try:
        # Create a temporary directory for output
        temp_output_dir = tempfile.mkdtemp()

        # Split the file
        chunks = split_file_into_chunks(
            temp_source_path, 
            chunk_size='1MB', 
            output_dir=temp_output_dir
        )

        # Verify chunks
        assert len(chunks) == 1
        assert os.path.exists(chunks[0])
        assert os.path.getsize(chunks[0]) == 100

    finally:
        # Clean up
        os.unlink(temp_source_path)
        shutil.rmtree(temp_output_dir)

def test_file_chunking_error_handling():
    """Test error handling in file chunking."""
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        split_file_into_chunks('/path/to/nonexistent/file.txt')

    # Test invalid chunk size
    with pytest.raises(ValueError):
        split_file_into_chunks(__file__, chunk_size=0)
    with pytest.raises(ValueError):
        split_file_into_chunks(__file__, chunk_size=-1)

def test_file_chunking_prefix():
    """Test custom prefix for chunk files."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b'0' * (1024 * 1024 * 2))  # 2MB file
        temp_source_path = temp_source.name

    try:
        # Create a temporary directory for output
        temp_output_dir = tempfile.mkdtemp()

        # Split the file with custom prefix
        chunks = split_file_into_chunks(
            temp_source_path, 
            chunk_size='1MB', 
            output_dir=temp_output_dir,
            prefix='custom_'
        )

        # Verify chunks have custom prefix
        assert all('custom_' in os.path.basename(chunk) for chunk in chunks)

    finally:
        # Clean up
        os.unlink(temp_source_path)
        shutil.rmtree(temp_output_dir)

def test_file_chunking_default_output_dir():
    """Test chunking a file when no output directory is specified."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix='.testchunk') as temp_source:
        temp_source.write(b'0' * (1024 * 1024 * 2))  # 2MB file
        temp_source_path = temp_source.name

    try:
        # Split the file
        chunks = split_file_into_chunks(temp_source_path, chunk_size='1MB')

        # Verify chunks are in the same directory as source file
        source_dir = os.path.dirname(temp_source_path)
        assert all(os.path.dirname(chunk) == source_dir for chunk in chunks)

    finally:
        # Clean up chunks and source file
        os.unlink(temp_source_path)
        for chunk in chunks:
            os.unlink(chunk)