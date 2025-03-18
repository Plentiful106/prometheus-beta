import pytest
from src.search_matrix import search_sorted_matrix

def test_search_matrix_basic_scenario():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Test single row matrix
    single_row_matrix = [[1, 2, 3, 4, 5]]
    assert search_sorted_matrix(single_row_matrix, 3) == True
    assert search_sorted_matrix(single_row_matrix, 6) == False

    # Test single column matrix
    single_col_matrix = [[1], [2], [3], [4], [5]]
    assert search_sorted_matrix(single_col_matrix, 3) == True
    assert search_sorted_matrix(single_col_matrix, 6) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # Test first and last elements
    assert search_sorted_matrix(matrix, 1) == True
    assert search_sorted_matrix(matrix, 60) == True

def test_search_matrix_invalid_input():
    with pytest.raises(ValueError):
        search_sorted_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_sorted_matrix(None, 5)

def test_search_matrix_large_range():
    large_matrix = [
        [1, 100, 200, 300],
        [400, 500, 600, 700],
        [800, 900, 1000, 1100]
    ]
    assert search_sorted_matrix(large_matrix, 600) == True
    assert search_sorted_matrix(large_matrix, 250) == False