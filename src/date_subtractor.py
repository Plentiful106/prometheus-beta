from datetime import datetime, timedelta

def subtract_days_from_date(date: datetime, days: int) -> datetime:
    """
    Subtract a specified number of days from a given date.

    Args:
        date (datetime): The original date to subtract days from.
        days (int): The number of days to subtract. Must be a non-negative integer.

    Returns:
        datetime: A new datetime object representing the date after subtraction.

    Raises:
        ValueError: If days is negative or not an integer.
        TypeError: If date is not a datetime object or days is not an integer.
    """
    # Type checking
    if not isinstance(date, datetime):
        raise TypeError("First argument must be a datetime object")
    
    if not isinstance(days, int):
        raise TypeError("Days must be an integer")
    
    # Check for negative days
    if days < 0:
        raise ValueError("Number of days to subtract must be non-negative")
    
    # Subtract days and return new datetime
    return date - timedelta(days=days)