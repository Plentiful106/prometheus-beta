import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_arr = [3, 1, 2, 4]
    expected = [1, 3, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_list():
    """Test empty list input"""
    assert sort_array_with_even_squares([]) == []

def test_only_odd_numbers():
    """Test list with only odd numbers"""
    input_arr = [5, 3, 1, 7]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_only_even_numbers():
    """Test list with only even numbers"""
    input_arr = [6, 2, 4, 8]
    expected = [64, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_mixed_numbers():
    """Test list with mixed odd and even numbers"""
    input_arr = [3, 1, 2, 4, 6, 5]
    expected = [1, 3, 5, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_duplicate_numbers():
    """Test list with duplicate numbers"""
    input_arr = [3, 2, 2, 1, 4]
    expected = [1, 3, 16, 4, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_negative_numbers():
    """Test list with negative numbers"""
    input_arr = [-3, -2, 1, 4, -1]
    expected = [-3, -1, 1, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")
    with pytest.raises(TypeError):
        sort_array_with_even_squares(123)
    with pytest.raises(TypeError):
        sort_array_with_even_squares(None)