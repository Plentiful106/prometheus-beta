import pytest
from src.matrix_search import search_matrix

def test_search_matrix_normal_cases():
    # Test cases where target exists
    matrix1 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_matrix(matrix1, 9) == True
    assert search_matrix(matrix1, 1) == True
    assert search_matrix(matrix1, 17) == True

    # Test cases where target does not exist
    assert search_matrix(matrix1, 2) == False
    assert search_matrix(matrix1, 10) == False
    assert search_matrix(matrix1, 20) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    assert search_matrix([[], []], 5) == False

    # Single element matrix
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 6) == False

def test_search_matrix_error_cases():
    # Invalid matrix types
    with pytest.raises(TypeError):
        search_matrix(None, 5)
    
    with pytest.raises(TypeError):
        search_matrix("not a matrix", 5)
    
    with pytest.raises(TypeError):
        search_matrix([[1, 2], ['a', 'b']], 5)

def test_search_matrix_with_floats():
    # Test with float values
    matrix = [[1.5, 2.7], [3.2, 4.1]]
    assert search_matrix(matrix, 2.7) == True
    assert search_matrix(matrix, 5.0) == False