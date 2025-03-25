import pytest
import brotli
from src.brotli_compression import brotli_compress, brotli_decompress

def test_brotli_compress_string():
    """Test compressing a string."""
    input_str = "Hello, world! This is a test of Brotli compression."
    compressed = brotli_compress(input_str)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(input_str.encode('utf-8'))

def test_brotli_compress_bytes():
    """Test compressing bytes."""
    input_bytes = b"Binary data compression test"
    compressed = brotli_compress(input_bytes)
    assert isinstance(compressed, bytes)
    # For very small inputs, compression might not always reduce size
    # So we'll just check that compression works without raising an error

def test_brotli_decompress():
    """Test decompressing Brotli compressed data."""
    input_str = "Hello, world! This is a decompression test."
    compressed = brotli_compress(input_str)
    decompressed = brotli_decompress(compressed)
    assert decompressed.decode('utf-8') == input_str

def test_brotli_compress_quality():
    """Test different compression qualities."""
    input_str = "Test compression quality variations" * 100
    
    # Test lowest and highest quality
    low_quality = brotli_compress(input_str, quality=0)
    high_quality = brotli_compress(input_str, quality=11)
    
    assert len(low_quality) > len(high_quality)

def test_brotli_compress_invalid_type():
    """Test compression with invalid input type."""
    with pytest.raises(TypeError):
        brotli_compress(123)
    
    with pytest.raises(TypeError):
        brotli_compress(None)

def test_brotli_compress_invalid_quality():
    """Test compression with invalid quality."""
    with pytest.raises(ValueError):
        brotli_compress("test", quality=-1)
    
    with pytest.raises(ValueError):
        brotli_compress("test", quality=12)

def test_brotli_decompress_invalid_type():
    """Test decompression with invalid input type."""
    with pytest.raises(TypeError):
        brotli_decompress("not bytes")
    
    with pytest.raises(TypeError):
        brotli_decompress(123)

def test_brotli_decompress_invalid_data():
    """Test decompression with invalid compressed data."""
    with pytest.raises(brotli.error):
        brotli_decompress(b"invalid compressed data")

def test_roundtrip_compression():
    """Test full compression and decompression roundtrip."""
    original_texts = [
        "Short text",
        "Longer text with multiple words and some complexity",
        "Mixed 123 !@# symbols text",
        "äöü international characters"
    ]
    
    for text in original_texts:
        compressed = brotli_compress(text)
        decompressed = brotli_decompress(compressed)
        assert decompressed.decode('utf-8') == text