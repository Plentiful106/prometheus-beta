"""
Module for logging error messages to the console.
"""

def log_error(message):
    """
    Log an error message to the console.

    Args:
        message (str): The error message to log.

    Raises:
        TypeError: If the message is not a string.
        ValueError: If the message is an empty string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    if not message.strip():
        raise ValueError("Error message cannot be empty")
    
    # Log the error message to console
    print(f"ERROR: {message}")