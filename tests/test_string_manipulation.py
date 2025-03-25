import pytest
from src.string_manipulation import rotate_and_reverse

def test_basic_rotation_and_reverse():
    """Test basic rotation and reversal"""
    assert rotate_and_reverse('hello', 2) == 'lehol'
    assert rotate_and_reverse('python', 1) == 'ohtypn'

def test_zero_rotations():
    """Test when rotations is zero"""
    assert rotate_and_reverse('hello', 0) == 'olleh'

def test_full_length_rotations():
    """Test rotations equal to string length"""
    assert rotate_and_reverse('hello', 5) == 'olleh'
    assert rotate_and_reverse('hello', 10) == 'olleh'

def test_empty_string():
    """Test empty string input"""
    assert rotate_and_reverse('', 3) == ''

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        rotate_and_reverse(123, 2)
    
    with pytest.raises(TypeError, match="Rotations must be an integer"):
        rotate_and_reverse('hello', '2')

def test_negative_rotations():
    """Test negative rotation input"""
    with pytest.raises(ValueError, match="Rotations cannot be negative"):
        rotate_and_reverse('hello', -1)

def test_single_char_string():
    """Test rotation of single character string"""
    assert rotate_and_reverse('a', 3) == 'a'