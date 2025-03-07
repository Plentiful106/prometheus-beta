import pytest
from src.exponential_search import exponential_search

def test_exponential_search_basic():
    """Test basic functionality of exponential search."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3
    assert exponential_search(arr, 1) == 0
    assert exponential_search(arr, 15) == 7

def test_exponential_search_not_found():
    """Test when target is not in the list."""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 4) == -1
    assert exponential_search(arr, 16) == -1

def test_exponential_search_edge_cases():
    """Test edge cases like single element and repeating elements."""
    # Single element list
    assert exponential_search([5], 5) == 0
    assert exponential_search([5], 6) == -1
    
    # List with repeating elements
    arr = [1, 1, 2, 2, 3, 3, 4, 4]
    assert exponential_search(arr, 2) in [2, 3]

def test_exponential_search_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Empty list
    with pytest.raises(ValueError):
        exponential_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError):
        exponential_search("not a list", 5)

def test_exponential_search_large_list():
    """Test with a larger sorted list."""
    arr = list(range(1000))
    assert exponential_search(arr, 500) == 500
    assert exponential_search(arr, 999) == 999
    assert exponential_search(arr, 1000) == -1