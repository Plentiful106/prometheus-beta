import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test with a standard array and k value"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test with a single element array"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_all_same_elements():
    """Test with an array of identical elements"""
    arr = [2, 2, 2, 2, 2]
    assert max_subarray_sum(arr, 3) == 6

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr, 2) == -3

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers"""
    arr = [1, -3, 4, 2, -1, 5, -2]
    assert max_subarray_sum(arr, 3) == 10

def test_invalid_k_too_large():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 4)

def test_invalid_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_invalid_k_negative():
    """Test when k is negative"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, -1)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 1)

def test_invalid_input_types():
    """Test with invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list", 2)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        max_subarray_sum([1, 2, 3], "2")