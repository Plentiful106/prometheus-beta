from datetime import datetime, timezone

def timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch).

    Returns:
        str: A human-readable date string in the format 'YYYY-MM-DD HH:MM:SS UTC'.

    Raises:
        TypeError: If the input is not a numeric type.
        ValueError: If the timestamp is invalid or out of reasonable range.
    """
    # Check input type
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a numeric value")
    
    # Check timestamp validity (reasonable range: ~1970 to ~2100)
    try:
        # Convert timestamp to datetime object in UTC
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        
        # Format the datetime to a human-readable string
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    except (ValueError, OverflowError) as e:
        raise ValueError(f"Invalid timestamp: {e}")