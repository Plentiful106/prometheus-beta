from datetime import datetime

def get_day_name(date):
    """
    Return the name of the day for a given date.

    Args:
        date (str or datetime): The date to get the day name for. 
                                Can be a datetime object or a date string.

    Returns:
        str: The full name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input cannot be converted to a valid date
    """
    # If input is a string, try to convert it to a datetime object
    if isinstance(date, str):
        try:
            # Try multiple common date formats
            date_formats = [
                '%Y-%m-%d',  # ISO format
                '%m/%d/%Y',  # US format
                '%d/%m/%Y',  # UK format
                '%Y/%m/%d'   # Alternative ISO format
            ]
            
            for date_format in date_formats:
                try:
                    date = datetime.strptime(date, date_format)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(f"Unable to parse date from input: {date}")
        
        except Exception as e:
            raise ValueError(f"Invalid date format: {e}")
    
    # If input is a datetime object, ensure it's a valid date
    if not isinstance(date, datetime):
        raise ValueError("Input must be a string or datetime object")
    
    # Return the full day name
    return date.strftime('%A')