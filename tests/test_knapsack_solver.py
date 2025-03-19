import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack_problem():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items_list():
    """Test with an empty list of items"""
    items = []
    capacity = 10
    assert solve_knapsack(items, capacity) == 0

def test_zero_capacity():
    """Test with zero capacity"""
    items = [(1, 10), (2, 20), (3, 30)]
    capacity = 0
    assert solve_knapsack(items, capacity) == 0

def test_impossible_to_fill():
    """Test when items are too heavy for the capacity"""
    items = [(10, 100), (20, 200)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_single_item_fits():
    """Test with a single item that fits exactly"""
    items = [(5, 50)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 50

def test_multiple_optimal_combinations():
    """Test a scenario with multiple ways to maximize value"""
    items = [(1, 10), (3, 40), (4, 50), (5, 70)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 90

def test_invalid_negative_capacity():
    """Test error handling for negative capacity"""
    items = [(1, 10), (2, 20)]
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(items, -1)

def test_invalid_negative_weight():
    """Test error handling for negative item weights"""
    items = [(1, 10), (-2, 20)]
    with pytest.raises(ValueError, match="Item weights must be non-negative numbers"):
        solve_knapsack(items, 10)

def test_invalid_negative_value():
    """Test error handling for negative item values"""
    items = [(1, -10), (2, 20)]
    with pytest.raises(ValueError, match="Item values must be non-negative numbers"):
        solve_knapsack(items, 10)

def test_floating_point_inputs():
    """Test handling of floating-point weights and values"""
    items = [(1.5, 10.5), (2.3, 20.7)]
    capacity = 3
    assert solve_knapsack(items, capacity) == 20.7