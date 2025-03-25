import pytest
import sys
import os

# Ensure src directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sorting import sort_nums, optimal_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_list = [5, 2, 8, 1, 9]
    assert optimal_sort(input_list) == [1, 2, 5, 8, 9]

def test_sort_nums_bug():
    """Demonstrate the bug in sort_nums"""
    input_list = [5, 2, 8, 1, 9]
    result = sort_nums(input_list)
    # The result is likely to be incorrect due to the intentional bug
    assert result != [1, 2, 5, 8, 9]

def test_empty_list():
    """Test sorting an empty list"""
    assert optimal_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert optimal_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert optimal_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert optimal_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert optimal_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_numeric_types():
    """Test sorting with mixed numeric types"""
    input_list = [5.5, 2, 8, 1.1, 9]
    assert optimal_sort(input_list) == [1.1, 2, 5.5, 8, 9]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        optimal_sort("not a list")

def test_invalid_list_elements():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError):
        optimal_sort([1, 2, "three", 4])

def test_large_list():
    """Test sorting a larger list"""
    import random
    random.seed(42)  # For reproducibility
    large_list = [random.randint(1, 1000) for _ in range(1000)]
    assert optimal_sort(large_list) == sorted(large_list)