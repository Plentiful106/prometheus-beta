import pytest
from src.hyphen_replacer import replace_hyphens_with_spaces

def test_replace_hyphens_with_spaces_basic():
    """Test basic hyphen replacement."""
    assert replace_hyphens_with_spaces('hello-world') == 'hello world'

def test_replace_hyphens_with_spaces_multiple_hyphens():
    """Test replacing multiple hyphens."""
    assert replace_hyphens_with_spaces('hello-world-test') == 'hello world test'

def test_replace_hyphens_with_spaces_no_hyphens():
    """Test string with no hyphens."""
    assert replace_hyphens_with_spaces('helloworld') == 'helloworld'

def test_replace_hyphens_with_spaces_empty_string():
    """Test empty string."""
    assert replace_hyphens_with_spaces('') == ''

def test_replace_hyphens_with_spaces_error_non_string():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(123)

def test_replace_hyphens_with_spaces_consecutive_hyphens():
    """Test replacing consecutive hyphens."""
    assert replace_hyphens_with_spaces('hello----world') == 'hello    world'