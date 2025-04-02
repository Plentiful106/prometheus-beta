import time
import functools
import logging
from typing import Callable, Any

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_query_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log the execution time of database query methods.
    
    Args:
        func (Callable): The database query method to be timed and logged.
    
    Returns:
        Callable: Wrapped function with timing and logging.
    
    Raises:
        TypeError: If the decorated object is not a callable function.
    """
    if not callable(func):
        raise TypeError("Decorated object must be a callable function")
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Start timing
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate execution time
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            # Log the query execution time
            logger.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur during query execution
            logger.error(f"Error in query '{func.__name__}': {str(e)}")
            raise
    
    return wrapper