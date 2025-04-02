import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic_success():
    """Test finding an existing element in the matrix"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True

def test_matrix_search_basic_failure():
    """Test searching for a non-existing element"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 10) == False

def test_matrix_search_single_element_matrix_success():
    """Test matrix with a single element"""
    matrix = [[42]]
    assert search_matrix(matrix, 42) == True

def test_matrix_search_single_element_matrix_failure():
    """Test matrix with a single element, target not found"""
    matrix = [[42]]
    assert search_matrix(matrix, 43) == False

def test_matrix_search_empty_matrix_raises_error():
    """Test that empty matrix raises a ValueError"""
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        search_matrix([], 5)

def test_matrix_search_none_input_raises_error():
    """Test that None input raises a TypeError"""
    with pytest.raises(TypeError):
        search_matrix(None, 5)

def test_matrix_search_invalid_input_type_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError):
        search_matrix("not a matrix", 5)

def test_matrix_search_jagged_matrix_raises_error():
    """Test that a jagged matrix (rows of different lengths) raises a ValueError"""
    jagged_matrix = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8]
    ]
    with pytest.raises(ValueError, match="All rows must have the same length"):
        search_matrix(jagged_matrix, 5)

def test_matrix_search_large_matrix():
    """Test searching in a larger matrix"""
    large_matrix = [
        [x for x in range(1, 51)],
        [x for x in range(51, 101)],
        [x for x in range(101, 151)]
    ]
    assert search_matrix(large_matrix, 75) == True
    assert search_matrix(large_matrix, 200) == False