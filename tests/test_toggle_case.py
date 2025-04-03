import pytest
from src.toggle_case import toggle_case

def test_toggle_case_mixed_string():
    """Test toggling case for a mixed-case string."""
    assert toggle_case('Hello, World!') == 'hELLO, wORLD!'

def test_toggle_case_all_uppercase():
    """Test toggling case for an all-uppercase string."""
    assert toggle_case('PYTHON') == 'python'

def test_toggle_case_all_lowercase():
    """Test toggling case for an all-lowercase string."""
    assert toggle_case('python') == 'PYTHON'

def test_toggle_case_empty_string():
    """Test toggling case for an empty string."""
    assert toggle_case('') == ''

def test_toggle_case_numbers_and_symbols():
    """Test that numbers and symbols remain unchanged."""
    assert toggle_case('Hello123!@#') == 'hELLO123!@#'

def test_toggle_case_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        toggle_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        toggle_case(None)