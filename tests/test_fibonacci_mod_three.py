import pytest
from src.fibonacci_mod_three import generate_modified_fibonacci

def test_generate_modified_fibonacci_zero():
    """Test generating sequence with zero as input."""
    assert generate_modified_fibonacci(0) == []

def test_generate_modified_fibonacci_single():
    """Test generating sequence with single element limit."""
    assert generate_modified_fibonacci(1) == [1]

def test_generate_modified_fibonacci_small():
    """Test generating sequence with small limit."""
    assert generate_modified_fibonacci(2) == [1, 1]

def test_generate_modified_fibonacci_small_limit():
    """Test generating sequence with small limit."""
    result = generate_modified_fibonacci(10)
    assert result == [1, 1, 3, 6, 9]
    assert all((result[i-2] + result[i-1]) % 3 == 0 for i in range(2, len(result)))

def test_generate_modified_fibonacci_large_limit():
    """Test generating sequence with larger limit."""
    result = generate_modified_fibonacci(100)
    assert result[0] == 1
    assert result[1] == 1
    assert all((result[i-2] + result[i-1]) % 3 == 0 for i in range(2, len(result)))

def test_divisibility_condition():
    """Verify that the sequence satisfies the divisibility condition."""
    sequence = generate_modified_fibonacci(50)
    assert all((sequence[i-2] + sequence[i-1]) % 3 == 0 for i in range(2, len(sequence)))

def test_invalid_input_negative():
    """Test handling of negative input."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_modified_fibonacci(-1)

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_modified_fibonacci("not an integer")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_modified_fibonacci(3.14)