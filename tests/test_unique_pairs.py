import pytest
from src.unique_pairs import get_unique_pairs

def test_get_unique_pairs_normal_case():
    """Test with a normal list of integers"""
    input_list = [1, 2, 3, 4]
    expected_pairs = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
    assert set(get_unique_pairs(input_list)) == set(expected_pairs)

def test_get_unique_pairs_with_duplicates():
    """Test with a list containing duplicate elements"""
    input_list = [1, 2, 2, 3, 3, 4]
    expected_pairs = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
    assert set(get_unique_pairs(input_list)) == set(expected_pairs)

def test_get_unique_pairs_empty_list():
    """Test with an empty list"""
    input_list = []
    assert get_unique_pairs(input_list) == []

def test_get_unique_pairs_single_element():
    """Test with a list containing only one element"""
    input_list = [5]
    assert get_unique_pairs(input_list) == []

def test_get_unique_pairs_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_pairs("not a list")

def test_get_unique_pairs_non_integer_elements():
    """Test with non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        get_unique_pairs([1, 2, "3", 4])

def test_get_unique_pairs_sorted_pairs():
    """Test that pairs are always sorted"""
    input_list = [4, 1, 2, 3]
    expected_pairs = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
    assert set(get_unique_pairs(input_list)) == set(expected_pairs)