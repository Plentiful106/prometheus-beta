import pytest
import math
from src.fibonacci_square_sum import generate_fibonacci_square_sum_sequence

def is_perfect_square(n):
    """Helper function to check if a number is a perfect square."""
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def test_generate_fibonacci_square_sum_sequence_basic():
    """Test basic functionality of the sequence generator."""
    sequence = generate_fibonacci_square_sum_sequence(5)
    assert len(sequence) == 5
    
    # Check that each consecutive pair sum is a perfect square
    for i in range(2, len(sequence)):
        pair_sum = sequence[i-1] + sequence[i]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_sum_sequence_single_element():
    """Test sequence generation with a single element."""
    sequence = generate_fibonacci_square_sum_sequence(1)
    assert sequence == [1]

def test_generate_fibonacci_square_sum_sequence_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Number of elements must be at least 1"):
        generate_fibonacci_square_sum_sequence(0)
    
    with pytest.raises(ValueError, match="Number of elements must be at least 1"):
        generate_fibonacci_square_sum_sequence(-1)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_square_sum_sequence(1.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_square_sum_sequence("5")

def test_generate_fibonacci_square_sum_sequence_sequence_properties():
    """Additional tests for sequence properties."""
    sequence = generate_fibonacci_square_sum_sequence(10)
    
    # Verify non-negative numbers
    assert all(num > 0 for num in sequence)
    
    # Check consecutive pair sums
    for i in range(2, len(sequence)):
        pair_sum = sequence[i-1] + sequence[i]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"