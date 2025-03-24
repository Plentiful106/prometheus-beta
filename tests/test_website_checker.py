import pytest
import requests
from src.website_checker import is_website_online

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

def test_valid_online_website(monkeypatch):
    """Test a website that is online with a 200 OK status."""
    def mock_get(*args, **kwargs):
        return MockResponse(200)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com') is True

def test_valid_online_website_redirect(monkeypatch):
    """Test a website that is online with a redirect status."""
    def mock_get(*args, **kwargs):
        return MockResponse(302)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com') is True

def test_website_connection_error(monkeypatch):
    """Test handling of connection errors."""
    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.nonexistentwebsite12345.com') is False

def test_website_timeout_error(monkeypatch):
    """Test handling of timeout errors."""
    def mock_get(*args, **kwargs):
        raise requests.exceptions.Timeout()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com', timeout=0.1) is False

def test_invalid_url_input():
    """Test handling of invalid URL inputs."""
    with pytest.raises(ValueError):
        is_website_online('')
    
    with pytest.raises(ValueError):
        is_website_online(None)

def test_website_server_error(monkeypatch):
    """Test websites with server errors."""
    def mock_get(*args, **kwargs):
        return MockResponse(500)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    assert is_website_online('https://www.example.com') is False