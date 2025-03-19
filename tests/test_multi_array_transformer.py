import pytest
from src.multi_array_transformer import transform_multi_array

def test_transform_multi_array_basic():
    """Test basic multi-array transformation."""
    input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_with_empty_subarrays():
    """Test transformation with empty sub-arrays."""
    input_array = [[1, 2], [], [3, 4], []]
    expected = [4, 3, 2, 1]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_with_duplicates():
    """Test transformation with duplicate elements."""
    input_array = [[1, 2, 2], [3, 3, 4], [5, 1]]
    expected = [4, 3, 2, 1, 5]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_complex():
    """Test a more complex transformation scenario."""
    input_array = [[1, 2], [3, 3, 4], [], [5, 1, 2], [6]]
    expected = [6, 2, 1, 5, 4, 3, 2, 1]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_empty_input():
    """Test transformation with an empty input array."""
    input_array = []
    expected = []
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_nested_types():
    """Test transformation with nested types and mixed elements."""
    input_array = [[1, 'a'], ['b', 2], [3, 'a', 'c']]
    expected = ['c', 'a', 2, 'b', 1]
    assert transform_multi_array(input_array) == expected