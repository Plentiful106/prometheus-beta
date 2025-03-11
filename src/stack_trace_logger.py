import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    logger: Optional[logging.Logger] = None, 
    log_level: int = logging.ERROR
) -> str:
    """
    Log a stack trace for an exception or the current stack trace.

    Args:
        exception (Optional[Exception]): The exception to log. If None, logs current stack trace.
        logger (Optional[logging.Logger]): Logger to use. If None, uses root logger.
        log_level (int): Logging level to use. Defaults to logging.ERROR.

    Returns:
        str: The formatted stack trace as a string.
    
    Examples:
        # Log current stack trace
        stack_trace = log_stack_trace()
        
        # Log a specific exception
        try:
            raise ValueError("An error occurred")
        except ValueError as e:
            stack_trace = log_stack_trace(e)
    """
    # Use root logger if no logger provided
    if logger is None:
        logger = logging.getLogger()

    # Get stack trace as string
    if exception is not None:
        # If an exception is provided, use its traceback
        stack_trace = ''.join(traceback.format_exception(
            type(exception), 
            exception, 
            exception.__traceback__
        ))
    else:
        # If no exception, get current stack trace
        stack_trace = ''.join(traceback.format_stack())

    # Log the stack trace
    logger.log(log_level, stack_trace)

    return stack_trace