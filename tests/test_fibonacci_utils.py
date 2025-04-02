import pytest
from src.fibonacci_utils import fibonacci, fibonacciSum

def test_fibonacci_basic():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(1) == [1]
    assert fibonacci(2) == [1, 1]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(0) == []

def test_fibonacci_edge_cases():
    """Test edge cases for Fibonacci sequence generation"""
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci("not a number")

def test_fibonacci_sum_basic():
    """Test basic functionality of fibonacciSum"""
    assert fibonacciSum([1]) == 1
    assert fibonacciSum([2]) == 2
    assert fibonacciSum([5]) == 7  # 1 + 1 + 2 + 3
    assert fibonacciSum([10]) == 17  # 1 + 1 + 2 + 3 + 5 + 8

def test_fibonacci_sum_multiple_numbers():
    """Test fibonacciSum with multiple input numbers"""
    assert fibonacciSum([2, 5]) == 7
    assert fibonacciSum([10, 20]) == 32  # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21

def test_fibonacci_sum_edge_cases():
    """Test edge cases and error handling for fibonacciSum"""
    with pytest.raises(ValueError):
        fibonacciSum([])
    with pytest.raises(ValueError):
        fibonacciSum([-1, 2, 3])
    with pytest.raises(ValueError):
        fibonacciSum("not a list")
    with pytest.raises(ValueError):
        fibonacciSum([1, "not a number", 3])

def test_fibonacci_sum_large_input():
    """Test fibonacciSum with larger input"""
    assert fibonacciSum([100]) == 88  # Sum of Fibonacci numbers <= 100