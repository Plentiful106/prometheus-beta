import time
import requests
import logging
from typing import Dict, Any, Optional

def log_network_request_response_time(
    url: str, 
    method: str = 'GET', 
    timeout: float = 10.0, 
    headers: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """
    Send a network request and log its response time.

    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method. Defaults to 'GET'
        timeout (float, optional): Request timeout in seconds. Defaults to 10.0
        headers (dict, optional): Additional headers for the request. Defaults to None

    Returns:
        Dict[str, Any]: A dictionary containing request details and response time

    Raises:
        ValueError: If an invalid URL or method is provided
        requests.RequestException: For network-related errors
    """
    # Validate inputs
    if not url or not isinstance(url, str):
        raise ValueError("A valid URL must be provided")
    
    method = method.upper()
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
    if method not in valid_methods:
        raise ValueError(f"Invalid HTTP method. Must be one of {valid_methods}")

    # Prepare headers (use empty dict if None)
    headers = headers or {}

    # Log the start of the request
    logging.info(f"Sending {method} request to {url}")

    # Track start time
    start_time = time.time()

    try:
        # Send the request
        response = requests.request(
            method=method, 
            url=url, 
            headers=headers, 
            timeout=timeout
        )

        # Calculate response time
        response_time = time.time() - start_time

        # Log successful request details
        logging.info(f"Request completed in {response_time:.4f} seconds")

        # Return comprehensive request information
        return {
            'url': url,
            'method': method,
            'status_code': response.status_code,
            'response_time': response_time,
            'headers': dict(response.headers)
        }

    except requests.RequestException as e:
        # Log and re-raise network-related exceptions
        logging.error(f"Network request failed: {str(e)}")
        raise