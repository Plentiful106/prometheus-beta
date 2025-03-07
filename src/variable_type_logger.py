import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.

    Args:
        variable: Any Python object whose type needs to be logged.

    Returns:
        str: The string representation of the variable's type.
    """
    # Get the type of the variable
    var_type = type(variable).__name__
    
    # Use a logger with a name specific to this module
    logger = logging.getLogger('variable_type_logger')
    
    # Only add handler if no handlers exist to prevent duplicate logs
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    # Log the type of the variable
    logger.info(f"Variable type: {var_type}")
    
    return var_type