from datetime import datetime

def convert_timestamp_to_readable_date(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): A Unix timestamp (seconds since epoch).

    Returns:
        str: A human-readable date string in the format 'Month Day, Year'.

    Raises:
        TypeError: If the input is not a number (int or float).
        ValueError: If the timestamp is negative or cannot be converted.
    """
    # Validate input type
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number (int or float)")
    
    # Validate timestamp value
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    try:
        # Convert timestamp to datetime object
        date_obj = datetime.fromtimestamp(timestamp)
        
        # Format date as a human-readable string
        return date_obj.strftime("%B %d, %Y")
    except (ValueError, OverflowError):
        raise ValueError("Invalid timestamp: Unable to convert to date")