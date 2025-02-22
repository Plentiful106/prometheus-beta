import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if a given string is a valid URL.
    
    Args:
        url (str): The URL string to validate
    
    Returns:
        bool: True if the URL is valid, False otherwise
    """
    if not isinstance(url, str):
        return False
    
    # Remove leading/trailing whitespace
    url = url.strip()
    
    # Check if the URL is empty
    if not url:
        return False
    
    try:
        # Use urlparse to check basic URL structure
        result = urlparse(url)
        
        # Check if scheme and netloc are present
        # Schemes like http, https, ftp, etc.
        valid_schemes = ['http', 'https', 'ftp', 'sftp']
        
        # Check if netloc is a valid hostname or localhost
        hostname_regex = r'^(localhost|[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+)$'
        
        return (
            result.scheme in valid_schemes and 
            result.netloc and 
            re.match(hostname_regex, result.netloc.split(':')[0]) is not None
        )
    except Exception:
        return False