import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating a basic triangle sequence."""
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_zero():
    """Test generating sequence with zero elements."""
    assert generate_triangle_sequence(0) == []

def test_generate_triangle_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of sequence elements must be non-negative"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_non_integer_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("5")

def test_generate_triangle_sequence_large_input():
    """Test generating a larger sequence."""
    result = generate_triangle_sequence(10)
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert result == expected

def test_triangle_sequence_properties():
    """Verify some mathematical properties of the triangle sequence."""
    sequence = generate_triangle_sequence(7)
    
    # Check that each number is the sum of consecutive integers
    assert sequence[0] == 1  # 1
    assert sequence[1] == 3  # 1 + 2
    assert sequence[2] == 6  # 1 + 2 + 3
    assert sequence[3] == 10  # 1 + 2 + 3 + 4
    assert sequence[4] == 15  # 1 + 2 + 3 + 4 + 5
    assert sequence[5] == 21  # 1 + 2 + 3 + 4 + 5 + 6
    assert sequence[6] == 28  # 1 + 2 + 3 + 4 + 5 + 6 + 7