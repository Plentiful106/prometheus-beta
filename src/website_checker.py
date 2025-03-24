import requests
import urllib3

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online and accessible.

    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (float, optional): Maximum time to wait for a response. Defaults to 5.0 seconds.

    Returns:
        bool: True if the website is online, False otherwise.

    Raises:
        ValueError: If the provided URL is invalid or empty.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    # Disable SSL warning for self-signed certificates
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        # Attempt to connect to the website
        response = requests.get(
            url, 
            timeout=timeout, 
            verify=False,  # Ignore SSL certificate verification
            allow_redirects=True
        )
        
        # Check if the request was successful (status code 200-399)
        return 200 <= response.status_code < 400
    
    except (
        requests.exceptions.ConnectionError,  # DNS failure, refused connection
        requests.exceptions.Timeout,          # Connection timeout
        requests.exceptions.RequestException  # Other request-related errors
    ):
        return False