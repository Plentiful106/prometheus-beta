import pytest
from src.unique_even_filter import filter_unique_even_numbers

def test_filter_unique_even_numbers_basic():
    """Test basic functionality of filtering unique even numbers"""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4, 8]
    expected = [2, 4, 6, 8]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_empty_list():
    """Test filtering an empty list"""
    assert filter_unique_even_numbers([]) == []

def test_filter_unique_even_numbers_no_evens():
    """Test list with no even numbers"""
    input_list = [1, 3, 5, 7]
    assert filter_unique_even_numbers(input_list) == []

def test_filter_unique_even_numbers_only_evens():
    """Test list with only even numbers"""
    input_list = [2, 4, 6, 8, 2, 4, 6, 8]
    expected = [2, 4, 6, 8]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_order_preservation():
    """Test that original order of first appearance is preserved"""
    input_list = [8, 2, 4, 6, 2, 8, 10, 4]
    expected = [8, 2, 4, 6, 10]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_negative_numbers():
    """Test handling of negative even numbers"""
    input_list = [-2, 1, -4, 3, -2, -4, 5]
    expected = [-2, -4]
    assert filter_unique_even_numbers(input_list) == expected