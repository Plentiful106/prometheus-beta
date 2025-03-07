import logging
import functools

def log_validation_message(severity='warning'):
    """
    Decorator to log input validation messages for function parameters.
    
    Args:
        severity (str, optional): Logging severity level. 
                                  Defaults to 'warning'.
                                  Supports 'debug', 'info', 'warning', 'error', 'critical'.
    
    Returns:
        Decorator function for logging validation messages.
    
    Raises:
        ValueError: If an invalid severity level is provided.
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Validate severity level
    valid_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    
    if severity not in valid_levels:
        raise ValueError(f"Invalid severity level. Choose from {list(valid_levels.keys())}")
    
    log_func = valid_levels[severity]
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log validation messages for each argument
            for i, arg in enumerate(args):
                if arg is None:
                    log_func(f"Argument {i} is None in function {func.__name__}")
                elif not arg:
                    log_func(f"Argument {i} is empty/falsy in function {func.__name__}")
            
            for key, value in kwargs.items():
                if value is None:
                    log_func(f"Keyword argument {key} is None in function {func.__name__}")
                elif not value:
                    log_func(f"Keyword argument {key} is empty/falsy in function {func.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator