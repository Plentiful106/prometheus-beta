"""
Unit tests for LZJH compression algorithm implementation.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzjh_compression import compress, decompress

def test_compress_basic():
    """Test basic compression and decompression"""
    original = b"hello world hello world"
    compressed = compress(original)
    assert compressed != original
    assert len(compressed) < len(original)
    
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_string():
    """Test compression with string input"""
    original = "hello world hello world"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_empty_input():
    """Test compression with empty input"""
    with pytest.raises(ValueError):
        compress(b"")
    with pytest.raises(ValueError):
        compress("")

def test_compress_invalid_input():
    """Test compression with invalid input types"""
    with pytest.raises(TypeError):
        compress(123)
    with pytest.raises(TypeError):
        compress(None)

def test_decompress_empty_input():
    """Test decompression with empty input"""
    with pytest.raises(ValueError):
        decompress(b"")

def test_decompress_invalid_input():
    """Test decompression with invalid input types"""
    with pytest.raises(TypeError):
        decompress("not bytes")
    with pytest.raises(TypeError):
        decompress(123)

def test_compress_decompress_repetitive():
    """Test compression and decompression with repetitive data"""
    original = b"AAAAAAAAAABBBBBBBBCCCCCCCC"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_decompress_mixed_data():
    """Test compression and decompression with mixed data"""
    original = b"abcdefghijklmnopqrstuvwxyz" * 10
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_large_input():
    """Test compression with a larger input"""
    original = b"Test data " * 1000
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original