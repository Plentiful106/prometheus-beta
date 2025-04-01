import pytest
import json
from src.api_json_parser import parse_api_json_response

def test_parse_json_string():
    """Test parsing a valid JSON string."""
    json_str = '{"name": "John", "age": 30}'
    result = parse_api_json_response(json_str)
    assert result == {"name": "John", "age": 30}

def test_parse_existing_dict():
    """Test parsing an already parsed dictionary."""
    input_dict = {"name": "Jane", "city": "New York"}
    result = parse_api_json_response(input_dict)
    assert result == input_dict

def test_invalid_json_string():
    """Test parsing an invalid JSON string."""
    with pytest.raises(ValueError, match="Invalid JSON string"):
        parse_api_json_response("Not a valid JSON")

def test_invalid_input_type():
    """Test parsing with an invalid input type."""
    with pytest.raises(TypeError, match="Response must be a JSON string or a dictionary"):
        parse_api_json_parser(42)  # Integer is not a valid input

def test_nested_json():
    """Test parsing a nested JSON structure."""
    nested_json_str = '{"user": {"name": "Alice", "details": {"age": 25, "active": true}}}'
    result = parse_api_json_response(nested_json_str)
    assert result == {"user": {"name": "Alice", "details": {"age": 25, "active": True}}}

def test_empty_json():
    """Test parsing an empty JSON object."""
    empty_json_str = '{}'
    result = parse_api_json_response(empty_json_str)
    assert result == {}