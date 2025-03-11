import sys
import io
from typing import Literal, Optional, Union, TextIO

class ColorLogger:
    """
    A utility class for logging messages in different colors to the console.
    
    Supports ANSI color codes for terminal output with optional fallback for 
    environments that don't support color.
    """
    
    # ANSI color codes
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    
    @classmethod
    def log(
        cls, 
        message: str, 
        color: Optional[Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']] = None, 
        file: Union[TextIO, None] = sys.stdout
    ) -> None:
        """
        Log a message in a specified color.
        
        Args:
            message (str): The message to log.
            color (Optional[str]): The color to use for logging. 
                                   Must be one of: red, green, yellow, blue, magenta, cyan, white.
            file (file object, optional): The file to write to. Defaults to sys.stdout.
        
        Raises:
            ValueError: If an invalid color is provided.
        """
        # Validate input
        if message is None:
            raise ValueError("Message cannot be None")
        
        if color is not None and color not in cls.COLORS:
            raise ValueError(f"Invalid color. Must be one of {list(cls.COLORS.keys())}")
        
        # Check if we should use color
        use_color = color and (
            (file == sys.stdout and sys.stdout.isatty()) or  # terminal stdout
            (file != sys.stdout and color is not None)  # custom file and color specified
        )
        
        # Prepare the output
        if use_color:
            colored_message = f"{cls.COLORS[color]}{message}{cls.COLORS['reset']}"
        else:
            colored_message = message
        
        # Write to file
        print(colored_message, file=file, flush=True)