import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that generated UUID matches the correct format."""
    uuid = generate_uuid()
    
    # Regex for UUID v4 format
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"UUID {uuid} does not match expected format"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set(generate_uuid() for _ in range(1000))
    
    assert len(uuids) == 1000, "Generated UUIDs are not unique"

def test_uuid_length():
    """Test that generated UUID has correct length."""
    uuid = generate_uuid()
    
    assert len(uuid) == 36, f"UUID length is incorrect: {len(uuid)}"
    assert uuid.count('-') == 4, f"UUID does not have 4 hyphens: {uuid}"

def test_uuid_parts():
    """Test specific parts of the UUID."""
    uuid = generate_uuid()
    parts = uuid.split('-')
    
    # Check length of each part
    assert len(parts[0]) == 8
    assert len(parts[1]) == 4
    assert len(parts[2]) == 4
    assert len(parts[3]) == 4
    assert len(parts[4]) == 12
    
    # Check version (4 in 3rd part)
    assert parts[2][0] == '4'
    
    # Check variant (8, 9, A, or B in 4th part)
    assert parts[3][0] in ['8', '9', 'a', 'A', 'b', 'B']