import pytest
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_basic_string_encoding_decoding():
    # Test basic string compression and decompression
    input_data = "hello"
    encoded = arithmetic_encode(input_data)
    
    assert 'compressed_value' in encoded
    assert 'frequency_table' in encoded
    
    decoded = arithmetic_decode(encoded, len(input_data))
    assert decoded == list(input_data)

def test_basic_list_encoding_decoding():
    # Test basic list compression and decompression
    input_data = [1, 2, 3, 2, 1]
    encoded = arithmetic_encode(input_data)
    
    assert 'compressed_value' in encoded
    assert 'frequency_table' in encoded
    
    decoded = arithmetic_decode(encoded, len(input_data))
    assert decoded == input_data

def test_empty_input_raises_error():
    # Test that empty input raises a ValueError
    with pytest.raises(ValueError):
        arithmetic_encode([])
    
    with pytest.raises(ValueError):
        arithmetic_decode({}, 0)

def test_invalid_compressed_data():
    # Test handling of invalid compressed data
    with pytest.raises(ValueError):
        arithmetic_decode({}, 5)
    
    with pytest.raises(ValueError):
        arithmetic_decode(None, 5)

def test_single_symbol_encoding():
    # Test encoding and decoding of a single repeated symbol
    input_data = ['a', 'a', 'a', 'a', 'a']
    encoded = arithmetic_encode(input_data)
    decoded = arithmetic_decode(encoded, len(input_data))
    assert decoded == input_data

def test_complex_symbol_list():
    # Test encoding and decoding of a more complex symbol list
    input_data = ['x', 'y', 'z', 'x', 'y', 'z', 'x']
    encoded = arithmetic_encode(input_data)
    decoded = arithmetic_decode(encoded, len(input_data))
    assert decoded == input_data

def test_compressed_value_range():
    # Ensure compressed value is always between 0 and 1
    input_data = "test string"
    encoded = arithmetic_encode(input_data)
    
    compressed_value = encoded['compressed_value']
    assert 0 <= compressed_value <= 1, "Compressed value must be between 0 and 1"