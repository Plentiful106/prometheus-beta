import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores_basic():
    """Test basic space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_with_underscores_multiple_spaces():
    """Test replacing multiple spaces."""
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_with_underscores_leading_trailing_spaces():
    """Test replacing leading and trailing spaces."""
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_with_underscores_empty_string():
    """Test handling of empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_with_underscores_no_spaces():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_with_underscores_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)