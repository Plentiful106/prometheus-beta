import requests
from typing import Dict, Optional, Union

def send_get_request(url: str, 
                     headers: Optional[Dict[str, str]] = None, 
                     params: Optional[Dict[str, Union[str, int, float]]] = None, 
                     timeout: float = 10.0) -> Dict[str, Union[int, str, Dict]]:
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (Dict[str, str], optional): Optional HTTP headers to include in the request.
        params (Dict[str, Union[str, int, float]], optional): Optional query parameters to include in the request.
        timeout (float, optional): Request timeout in seconds. Defaults to 10.0 seconds.

    Returns:
        Dict[str, Union[int, str, Dict]]: A dictionary containing the response details:
            - 'status_code': HTTP status code of the response
            - 'text': Response body as text
            - 'headers': Response headers
            - 'json': Response body as JSON (if applicable)

    Raises:
        ValueError: If the URL is empty or invalid
        requests.HTTPError: For HTTP error status codes
        requests.RequestException: For network-related errors
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    # Send GET request
    response = requests.get(
        url, 
        headers=headers, 
        params=params, 
        timeout=timeout
    )

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Prepare response dictionary
    response_data = {
        'status_code': response.status_code,
        'text': response.text,
        'headers': dict(response.headers)
    }

    # Try to parse JSON if possible
    try:
        response_data['json'] = response.json()
    except ValueError:
        response_data['json'] = None

    return response_data