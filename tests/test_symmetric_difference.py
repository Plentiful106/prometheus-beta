import pytest
from src.symmetric_difference import symmetric_difference

def test_basic_symmetric_difference():
    """Test symmetric difference with basic lists"""
    result = symmetric_difference([1, 2, 3], [3, 4, 5])
    assert set(result) == {1, 2, 4, 5}

def test_empty_lists():
    """Test symmetric difference with empty lists"""
    result = symmetric_difference([], [])
    assert result == []

def test_one_empty_list():
    """Test symmetric difference with one empty list"""
    result = symmetric_difference([1, 2, 3], [])
    assert set(result) == {1, 2, 3}

def test_identical_lists():
    """Test symmetric difference with identical lists"""
    result = symmetric_difference([1, 2, 3], [1, 2, 3])
    assert result == []

def test_lists_with_duplicates():
    """Test symmetric difference with lists containing duplicates"""
    result = symmetric_difference([1, 1, 2, 3], [3, 3, 4, 5])
    assert set(result) == {1, 2, 4, 5}

def test_invalid_input_types():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        symmetric_difference("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        symmetric_difference([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError):
        symmetric_difference(123, 456)

def test_list_of_mixed_types():
    """Test symmetric difference with lists of mixed types"""
    result = symmetric_difference([1, 'a', 2], ['a', 3, 4])
    assert set(result) == {1, 2, 3, 4}