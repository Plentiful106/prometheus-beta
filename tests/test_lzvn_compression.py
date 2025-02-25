"""
Test suite for LZVN Compression Algorithm
"""

import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple list"""
    original_data = [1, 2, 3, 4, 5, 2, 3, 4, 5]
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_repeated_sequence_compression():
    """Test compression of data with repeated sequences"""
    original_data = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_bytes_input():
    """Test compression with bytes input"""
    original_data = bytes([1, 2, 3, 4, 5, 2, 3, 4, 5])
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert list(decompressed) == list(original_data)

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError):
        lzvn_compress([])
    
    with pytest.raises(ValueError):
        lzvn_decompress([])

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        lzvn_compress("not a list")
    
    with pytest.raises(TypeError):
        lzvn_decompress("not a list")

def test_long_repeated_sequence():
    """Test compression of very long repeated sequences"""
    original_data = [1] * 300
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_mixed_data_compression():
    """Test compression of mixed data with some repetitions"""
    original_data = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 5, 5, 5]
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_compressed_data_integrity():
    """Ensure compressed data is a valid list of integers"""
    original_data = [1, 2, 3, 4, 5, 2, 3, 4, 5]
    compressed = lzvn_compress(original_data)
    
    assert isinstance(compressed, list)
    assert all(isinstance(x, int) for x in compressed)