import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test various valid URL formats"""
    valid_urls = [
        'http://www.example.com',
        'https://example.com',
        'https://subdomain.example.co.uk',
        'http://localhost',
        'https://example.com/path',
        'https://example.com:8080',
        'ftp://files.example.com',
    ]
    for url in valid_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_urls():
    """Test various invalid URL formats"""
    invalid_urls = [
        '',  # Empty string
        '   ',  # Whitespace
        'not a url',
        'www.example.com',  # Missing scheme
        'http://',  # Incomplete URL
        'https:// ',  # Whitespace in URL
        123,  # Non-string input
        None,  # None input
    ]
    for url in invalid_urls:
        assert not is_valid_url(url), f"{url} should be invalid"

def test_edge_cases():
    """Test edge case URLs"""
    edge_cases = [
        'http://localhost:8000',
        'https://example.com/path/to/resource?param=value',
        'ftp://user:pass@example.com',
    ]
    for url in edge_cases:
        assert is_valid_url(url), f"{url} should be valid"

def test_url_schemes():
    """Test different URL schemes"""
    scheme_urls = [
        'http://example.com',
        'https://example.com',
        'ftp://example.com',
        'sftp://example.com',
    ]
    for url in scheme_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_schemes():
    """Test URLs with invalid schemes"""
    invalid_scheme_urls = [
        'ssh://example.com',
        'git://example.com',
        'file://example.com',
    ]
    for url in invalid_scheme_urls:
        assert not is_valid_url(url), f"{url} should be invalid"