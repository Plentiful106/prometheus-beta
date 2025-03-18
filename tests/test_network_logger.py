import pytest
import requests
import logging
from unittest.mock import patch
from src.network_logger import log_network_request_response_time

def test_successful_get_request():
    """Test a successful GET request"""
    with patch('requests.request') as mock_request:
        # Mock a successful response
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}

        # Call the function
        result = log_network_request_response_time('https://example.com')

        # Assertions
        assert 'url' in result
        assert 'method' in result
        assert 'status_code' in result
        assert 'response_time' in result
        assert result['method'] == 'GET'
        assert result['status_code'] == 200

def test_different_http_methods():
    """Test different HTTP methods"""
    methods = ['POST', 'PUT', 'DELETE', 'PATCH']
    
    for method in methods:
        with patch('requests.request') as mock_request:
            mock_response = mock_request.return_value
            mock_response.status_code = 200
            mock_response.headers = {}

            result = log_network_request_response_time('https://example.com', method=method)
            assert result['method'] == method

def test_invalid_method():
    """Test that an invalid HTTP method raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid HTTP method"):
        log_network_request_response_time('https://example.com', method='INVALID')

def test_invalid_url():
    """Test that an invalid URL raises a ValueError"""
    with pytest.raises(ValueError, match="A valid URL must be provided"):
        log_network_request_response_time('')

def test_request_exception():
    """Test handling of network request exceptions"""
    with patch('requests.request') as mock_request:
        # Simulate a network exception
        mock_request.side_effect = requests.RequestException("Network error")

        with pytest.raises(requests.RequestException):
            log_network_request_response_time('https://example.com')

def test_custom_headers():
    """Test sending custom headers"""
    with patch('requests.request') as mock_request:
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        mock_response.headers = {}

        custom_headers = {'Authorization': 'Bearer token123'}
        result = log_network_request_response_time(
            'https://example.com', 
            headers=custom_headers
        )

        # Verify the request was called with the custom headers
        mock_request.assert_called_once_with(
            method='GET', 
            url='https://example.com', 
            headers=custom_headers, 
            timeout=10.0
        )

def test_response_time_logged():
    """Verify that response time is logged"""
    with patch('requests.request'), patch('logging.info') as mock_log:
        log_network_request_response_time('https://example.com')
        
        # Check that a log message with response time was created
        assert any('Request completed in' in call[0][0] for call in mock_log.call_args_list)