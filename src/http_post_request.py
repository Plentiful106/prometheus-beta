import requests
from typing import Dict, Any, Optional

def send_http_post_request(
    url: str, 
    data: Optional[Dict[str, Any]] = None, 
    headers: Optional[Dict[str, str]] = None, 
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL to send the POST request to.
        data (dict, optional): A dictionary of data to send in the request body. Defaults to None.
        headers (dict, optional): A dictionary of HTTP headers to include. Defaults to None.
        timeout (int, optional): Maximum time in seconds to wait for the request. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.

    Raises:
        ValueError: If the URL is empty or invalid.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: Must be a non-empty string")

    # Set default headers if not provided
    if headers is None:
        headers = {'Content-Type': 'application/json'}

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return response details
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.json() if response.content else None
        }

    except requests.RequestException as e:
        # Handle and re-raise network-related exceptions
        raise RuntimeError(f"HTTP POST request failed: {str(e)}") from e