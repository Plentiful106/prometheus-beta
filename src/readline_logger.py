import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class for logging interactive readline prompts with configurable logging.
    
    This class provides methods to log user inputs during interactive sessions,
    with options for custom logging configuration and input validation.
    """
    
    def __init__(self, 
                 logger: Optional[logging.Logger] = None, 
                 log_level: int = logging.INFO):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): Custom logger. If None, creates a default logger.
            log_level (int): Logging level. Defaults to logging.INFO.
        """
        # Create a default logger if not provided
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(log_level)
        
        # Ensure there's a handler if no handlers exist
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)
    
    def log_input(self, 
                  prompt: str, 
                  validator: Optional[Callable[[str], bool]] = None) -> str:
        """
        Log an interactive input prompt with optional validation.
        
        Args:
            prompt (str): The prompt to display to the user.
            validator (Optional[Callable[[str], bool]]): Optional function to validate input.
        
        Returns:
            str: The validated user input.
        
        Raises:
            ValueError: If input validation fails.
        """
        while True:
            try:
                # Log the prompt
                self._logger.info(f"Prompt: {prompt}")
                
                # Get user input using readline
                user_input = input(prompt)
                
                # Log the input
                self._logger.info(f"Input received: {user_input}")
                
                # Validate input if a validator is provided
                if validator:
                    if not validator(user_input):
                        self._logger.warning("Input validation failed")
                        raise ValueError("Input does not meet validation criteria")
                
                return user_input
            
            except ValueError as ve:
                # Log validation errors
                self._logger.error(f"Validation error: {ve}")
                # Optionally could re-prompt or handle differently
                continue
            except Exception as e:
                # Log unexpected errors
                self._logger.error(f"Unexpected error during input: {e}")
                raise