import pytest
from src.multi_array_manipulator import multiArrayManipulator

def test_multiply_scalar():
    # Test multiplication by scalar
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'operation': 'multiply', 'value': 2})
    assert result == [[2, 4], [6, 8]]

def test_multiply_array():
    # Test multiplication by another array
    arr = [[1, 2], [3, 4]]
    matrix = [[2, 0], [1, 3]]
    result = multiArrayManipulator(arr, {'operation': 'multiply', 'value': matrix})
    assert result == [[4, 6], [10, 12]]

def test_add_scalar():
    # Test addition of scalar
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'operation': 'add', 'value': 2})
    assert result == [[3, 4], [5, 6]]

def test_add_array():
    # Test addition of another array
    arr = [[1, 2], [3, 4]]
    matrix = [[2, 3], [4, 5]]
    result = multiArrayManipulator(arr, {'operation': 'add', 'value': matrix})
    assert result == [[3, 5], [7, 9]]

def test_transpose():
    # Test array transposition
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {'operation': 'transpose'})
    assert result == [[1, 3], [2, 4]]

def test_no_operation():
    # Test no operation returns original array
    arr = [[1, 2], [3, 4]]
    result = multiArrayManipulator(arr, {})
    assert result == [[1, 2], [3, 4]]

def test_invalid_operation():
    # Test invalid operation raises ValueError
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Unsupported operation"):
        multiArrayManipulator(arr, {'operation': 'divide'})

def test_multiply_incompatible_dimensions():
    # Test multiply with incompatible array dimensions
    arr = [[1, 2], [3, 4]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Array dimensions incompatible"):
        multiArrayManipulator(arr, {'operation': 'multiply', 'value': matrix})

def test_add_incompatible_dimensions():
    # Test add with incompatible array dimensions
    arr = [[1, 2], [3, 4]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Arrays must have the same dimensions"):
        multiArrayManipulator(arr, {'operation': 'add', 'value': matrix})

def test_invalid_manipulations_type():
    # Test invalid manipulations type
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Manipulations must be a dictionary"):
        multiArrayManipulator(arr, "not a dict")