"""
Test suite for LZO compression and decompression functions.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import lzo_compress, lzo_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original_data = b"hello world hello world hello world"
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_repeated_pattern_compression():
    """Test compression of highly repetitive data."""
    original_data = b"ABCABCABCABCABCABCABCABC" * 10
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_random_data_compression():
    """Test compression of somewhat random data."""
    import os
    original_data = os.urandom(1024)
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        lzo_compress(b"")
    
    with pytest.raises(ValueError):
        lzo_decompress(b"")

def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        lzo_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzo_decompress("not bytes")

def test_single_byte_compression():
    """Test compression of a single byte."""
    original_data = b"A"
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data

def test_large_data_compression():
    """Test compression of larger data set."""
    original_data = b"Test data " * 1000
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data
    assert len(compressed) < len(original_data)

def test_binary_data_compression():
    """Test compression of binary data."""
    original_data = bytes([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5] * 100)
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data