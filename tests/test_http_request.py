import pytest
import requests
from unittest.mock import patch
from src.http_request import send_get_request

class MockResponse:
    def __init__(self, status_code=200, text='', headers=None, json_data=None):
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self._json = json_data

    def json(self):
        if self._json is None:
            raise ValueError("No JSON data")
        return self._json

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

def test_successful_get_request():
    """Test a successful GET request with a JSON response."""
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(
            status_code=200, 
            text='{"key": "value"}', 
            headers={'Content-Type': 'application/json'},
            json_data={'key': 'value'}
        )
        mock_get.return_value = mock_response

        result = send_get_request('https://example.com')
        assert result['status_code'] == 200
        assert result['text'] == '{"key": "value"}'
        assert result['json'] == {'key': 'value'}
        assert 'Content-Type' in result['headers']

def test_get_request_with_params_and_headers():
    """Test GET request with query parameters and custom headers."""
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=200, text='OK')
        mock_get.return_value = mock_response

        result = send_get_request(
            'https://example.com', 
            headers={'Authorization': 'Bearer token'},
            params={'id': 123}
        )
        assert result['status_code'] == 200

def test_get_request_without_json():
    """Test a request that returns non-JSON text."""
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=200, text='Plain text response')
        mock_get.return_value = mock_response

        result = send_get_request('https://example.com')
        assert result['status_code'] == 200
        assert result['text'] == 'Plain text response'
        assert result['json'] is None

def test_invalid_url_error():
    """Test error handling for invalid URL."""
    with pytest.raises(ValueError, match="Invalid URL"):
        send_get_request('')

def test_request_exception():
    """Test handling of request exceptions."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Connection error")

        with pytest.raises(RuntimeError, match="HTTP GET request failed"):
            send_get_request('https://example.com')

def test_http_error():
    """Test handling of HTTP error status codes."""
    with patch('requests.get') as mock_get:
        mock_response = MockResponse(status_code=404)
        mock_get.return_value = mock_response

        with pytest.raises(requests.HTTPError):
            send_get_request('https://example.com')

def test_timeout():
    """Test timeout functionality."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.Timeout("Request timed out")

        with pytest.raises(RuntimeError, match="HTTP GET request failed"):
            send_get_request('https://example.com', timeout=1.0)