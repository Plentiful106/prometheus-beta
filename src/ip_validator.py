def is_valid_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string represents a valid IPv4 address.
    
    Args:
        ip_string (str): The string to be validated as an IP address.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    
    Examples:
        >>> is_valid_ip_address('192.168.0.1')
        True
        >>> is_valid_ip_address('255.255.255.255')
        True
        >>> is_valid_ip_address('256.0.0.1')
        False
        >>> is_valid_ip_address('192.168.0')
        False
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the IP address into octets
    octets = ip_string.split('.')
    
    # Validate number of octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is a valid integer
        try:
            # Convert to integer and check range
            num = int(octet)
            if num < 0 or num > 255:
                return False
            
            # Ensure no leading zeros (except for 0 itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
        
        except ValueError:
            # Not a valid integer
            return False
    
    return True