import logging
import functools
import inspect

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
            # Get function signature to map positional and keyword arguments
            sig = inspect.signature(func)
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Log validation messages for each argument
            for name, value in bound_arguments.arguments.items():
                if value is None:
                    log_func(f"{name} is None in function {func.__name__}")
                elif not value and value is not False:
                    log_func(f"{name} is empty/falsy in function {func.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator