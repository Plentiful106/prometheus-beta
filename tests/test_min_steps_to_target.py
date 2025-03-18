import pytest
from src.min_steps_to_target import min_steps_to_target_sum

def test_basic_positive_scenario():
    """Test a basic scenario where target can be reached"""
    assert min_steps_to_target_sum([1, 2, 3], 4) == 2

def test_target_zero():
    """Test reaching target zero"""
    assert min_steps_to_target_sum([1, -1, 2, -2], 0) == 1

def test_negative_numbers():
    """Test scenario with negative numbers"""
    assert min_steps_to_target_sum([-1, 2, 3], 2) == 2

def test_impossible_target():
    """Test when target cannot be reached"""
    assert min_steps_to_target_sum([1, 3, 5], 10) is None

def test_single_number_matching_target():
    """Test when a single number matches the target"""
    assert min_steps_to_target_sum([5, 1, 2], 5) == 1

def test_multiple_ways_to_reach_target():
    """Test when multiple ways exist, returns minimum steps"""
    assert min_steps_to_target_sum([1, 2, 3, 4], 5) == 2

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        min_steps_to_target_sum([], 5)

def test_large_numbers():
    """Test with larger numbers"""
    assert min_steps_to_target_sum([10, 20, 30], 40) == 2

def test_repeated_numbers():
    """Test with repeated numbers"""
    assert min_steps_to_target_sum([1, 1, 2, 2], 3) == 2