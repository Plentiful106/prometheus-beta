import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        '0.0.0.0',
        '255.255.255.255',
        '192.168.0.1',
        '10.0.0.0',
        '172.16.0.1'
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        # Out of range
        '256.0.0.1',
        '0.0.0.256',
        
        # Incomplete addresses
        '192.168.0',
        '192.168',
        
        # Non-numeric
        '192.168.0.a',
        'abc.def.ghi.jkl',
        
        # Leading zeros
        '01.02.03.04',
        
        # Negative numbers
        '-1.0.0.0',
        
        # Wrong type
        123,
        None,
        '',
        '   '
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case scenarios."""
    # Empty string
    assert is_valid_ip_address('') == False
    
    # Spaces
    assert is_valid_ip_address(' 192.168.0.1 ') == False
    
    # Type checking
    assert is_valid_ip_address(None) == False
    assert is_valid_ip_address(123) == False