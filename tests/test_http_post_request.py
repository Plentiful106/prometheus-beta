import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

class MockResponse:
    def __init__(self, json_data, status_code, headers=None):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = headers or {}
        self.content = json_data is not None

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"HTTP Error: {self.status_code}")

def test_successful_post_request():
    test_url = "https://example.com/api"
    test_data = {"key": "value"}
    test_headers = {"Authorization": "Bearer token"}

    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data={"response": "success"}, 
            status_code=200, 
            headers={"Content-Type": "application/json"}
        )
        mock_post.return_value = mock_response

        result = send_http_post_request(test_url, data=test_data, headers=test_headers)

        mock_post.assert_called_once_with(
            test_url, 
            json=test_data, 
            headers=test_headers, 
            timeout=10
        )

        assert result['status_code'] == 200
        assert result['body'] == {"response": "success"}

def test_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        send_http_post_request("")

def test_empty_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        send_http_post_request(None)

def test_request_exception():
    test_url = "https://example.com/api"
    
    with patch('requests.post') as mock_post:
        mock_post.side_effect = requests.RequestException("Network error")

        with pytest.raises(RuntimeError, match="HTTP POST request failed"):
            send_http_post_request(test_url)

def test_default_headers():
    test_url = "https://example.com/api"

    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data={"response": "success"}, 
            status_code=200
        )
        mock_post.return_value = mock_response

        send_http_post_request(test_url)

        mock_post.assert_called_once_with(
            test_url, 
            json=None, 
            headers={'Content-Type': 'application/json'}, 
            timeout=10
        )

def test_no_response_body():
    test_url = "https://example.com/api"

    with patch('requests.post') as mock_post:
        mock_response = MockResponse(
            json_data=None, 
            status_code=204
        )
        mock_post.return_value = mock_response

        result = send_http_post_request(test_url)

        assert result['body'] is None