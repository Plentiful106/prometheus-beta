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
    
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Log the type of the variable
    logging.info(f"Variable type: {var_type}")
    
    return var_type