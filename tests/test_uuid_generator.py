import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str), "Result should be a string"

def test_generate_uuid_correct_format():
    """Test that the generated UUID matches the standard UUID v4 format."""
    # UUID v4 regex pattern
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    result = generate_uuid()
    assert re.match(uuid_pattern, result, re.IGNORECASE), "UUID does not match the expected format"

def test_generate_uuid_unique():
    """Test that multiple generated UUIDs are unique."""
    uuid_set = set()
    
    # Generate multiple UUIDs
    for _ in range(1000):
        uuid_set.add(generate_uuid())
    
    # Verify that all UUIDs are unique
    assert len(uuid_set) == 1000, "Generated UUIDs are not unique"