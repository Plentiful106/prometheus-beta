import os
import pytest
import tempfile
import zlib

from src.file_compression import calculate_compression_ratio

def test_compression_ratio_small_text():
    """Test compression ratio for a small text file"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, this is a test file!")
        temp_file.close()
    
    try:
        ratio = calculate_compression_ratio(temp_file.name)
        assert 0 < ratio < 1, f"Invalid compression ratio: {ratio}"
    finally:
        os.unlink(temp_file.name)

def test_compression_ratio_binary():
    """Test compression ratio for a binary file"""
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(os.urandom(1024))  # 1KB of random data
        temp_file.close()
    
    try:
        ratio = calculate_compression_ratio(temp_file.name)
        assert 0 < ratio < 1, f"Invalid compression ratio: {ratio}"
    finally:
        os.unlink(temp_file.name)

def test_empty_file_raises_error():
    """Test that an empty file raises a ValueError"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
    
    try:
        with pytest.raises(ValueError, match="Cannot calculate compression ratio for an empty file"):
            calculate_compression_ratio(temp_file.name)
    finally:
        os.unlink(temp_file.name)

def test_nonexistent_file_raises_error():
    """Test that a nonexistent file raises a FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        calculate_compression_ratio("/path/to/nonexistent/file.txt")

def test_compression_ratio_large_file():
    """Test compression ratio for a large file with repetitive content"""
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as temp_file:
        temp_file.write(b"REPEATED_DATA" * 10000)  # Large repetitive file
        temp_file.close()
    
    try:
        ratio = calculate_compression_ratio(temp_file.name)
        assert 0 < ratio < 1, f"Invalid compression ratio: {ratio}"
    finally:
        os.unlink(temp_file.name)