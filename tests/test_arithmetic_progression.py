import pytest
from src.arithmetic_progression import check_arithmetic_progression

def test_basic_arithmetic_progression():
    """Test a simple arithmetic progression"""
    assert check_arithmetic_progression([2, 4, 6, 8, 10]) == True

def test_arithmetic_progression_at_start():
    """Test arithmetic progression at the start of the array"""
    assert check_arithmetic_progression([1, 3, 5, 7, 9]) == True

def test_arithmetic_progression_at_end():
    """Test arithmetic progression at the end of the array"""
    assert check_arithmetic_progression([5, 7, 9, 11, 13]) == True

def test_no_arithmetic_progression():
    """Test array with no arithmetic progression"""
    assert check_arithmetic_progression([1, 2, 4, 8, 16]) == False

def test_minimum_length():
    """Test arrays shorter than 3 elements"""
    assert check_arithmetic_progression([1, 2]) == False
    assert check_arithmetic_progression([]) == False

def test_single_arithmetic_progression():
    """Test array with a single arithmetic progression"""
    assert check_arithmetic_progression([3, 5, 7, 1, 2]) == True

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        check_arithmetic_progression("not a list")
    with pytest.raises(TypeError):
        check_arithmetic_progression(123)

def test_invalid_element_type():
    """Test raising ValueError for non-positive or non-integer elements"""
    with pytest.raises(ValueError):
        check_arithmetic_progression([1, 2, -3])
    with pytest.raises(ValueError):
        check_arithmetic_progression([1, 2, 3.5])
    with pytest.raises(ValueError):
        check_arithmetic_progression([1, 2, '3'])