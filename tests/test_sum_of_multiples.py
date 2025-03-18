import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_sum_of_multiples():
    """Test basic functionality of sum_of_multiples."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10 = 23

def test_single_multiple():
    """Test with a single multiple."""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9 = 18

def test_unique_multiples():
    """Test that duplicates are not counted multiple times."""
    assert sum_of_multiples(10, [3, 6]) == 18  # 3 + 6 + 9 = 18

def test_edge_case_limit_exactly_matches_multiple():
    """Test when limit is exactly a multiple."""
    assert sum_of_multiples(12, [3, 5]) == 45  # 3 + 5 + 6 + 9 + 10 + 12 = 45

def test_empty_multiples_list():
    """Test with an empty list of multiples."""
    assert sum_of_multiples(10, []) == 0

def test_input_validation_non_positive_limit():
    """Test that ValueError is raised for non-positive limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(0, [3, 5])
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(-10, [3, 5])

def test_input_validation_non_positive_multiple():
    """Test that ValueError is raised for non-positive multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [0, 5])
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [-3, 5])

def test_large_numbers():
    """Test with larger numbers to ensure efficiency."""
    assert sum_of_multiples(1000, [3, 5]) == 234168