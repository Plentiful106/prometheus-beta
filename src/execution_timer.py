import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): A logger to use for recording execution time. 
                                           If not provided, uses the root logger.
    
    Returns:
        callable: A decorator function that logs execution time.
    
    Example:
        @log_execution_time()
        def example_function():
            time.sleep(1)  # Simulate some work
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log the execution time
                logger.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Error in function '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator