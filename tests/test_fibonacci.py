import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_numbers():
    """Test Fibonacci numbers for small inputs"""
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for n, expected in enumerate(expected_sequence):
        assert fibonacci(n) == expected

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger inputs"""
    # Known Fibonacci numbers for specific indices
    test_cases = [
        (10, 55),
        (20, 6765),
        (30, 832040),
        (40, 102334155)
    ]
    
    for n, expected in test_cases:
        assert fibonacci(n) == expected

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_time_complexity():
    """Verify that large Fibonacci numbers can be computed quickly"""
    import time
    
    start_time = time.time()
    result = fibonacci(100)
    end_time = time.time()
    
    # Verify the result for a large n
    assert result == 354224848179261915075
    
    # Compute time should be very quick (< 0.01 seconds)
    assert end_time - start_time < 0.01