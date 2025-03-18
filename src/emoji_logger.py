import logging
import emoji

class EmojiLogger:
    """
    A custom logger that supports logging messages with emojis.
    
    This logger extends Python's standard logging functionality by allowing
    easy insertion of emojis into log messages.
    """
    
    def __init__(self, name='EmojiLogger', level=logging.INFO):
        """
        Initialize the EmojiLogger.
        
        Args:
            name (str, optional): Name of the logger. Defaults to 'EmojiLogger'.
            level (int, optional): Logging level. Defaults to logging.INFO.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Create console handler if no handlers exist
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
    
    def log(self, level, message, emoji_name=None):
        """
        Log a message with an optional emoji.
        
        Args:
            level (int): Logging level (e.g., logging.INFO, logging.ERROR)
            message (str): The message to log
            emoji_name (str, optional): Name of the emoji to prepend to the message
        
        Raises:
            ValueError: If an invalid emoji name is provided
        """
        # Convert emoji_name to proper format
        if emoji_name:
            try:
                # Remove colons if present and standardize format
                clean_emoji_name = emoji_name.strip(':')
                emoji_symbol = emoji.emojize(f':{clean_emoji_name}:', language='alias')
                message = f'{emoji_symbol} {message}'
            except Exception:
                # Raise a custom error for invalid emoji
                raise ValueError(f"Invalid emoji name: {emoji_name}")
        
        # Log the message at the specified level
        self.logger.log(level, message)
    
    def info(self, message, emoji_name=None):
        """
        Log an INFO level message with an optional emoji.
        
        Args:
            message (str): The message to log
            emoji_name (str, optional): Name of the emoji to prepend
        """
        self.log(logging.INFO, message, emoji_name)
    
    def warning(self, message, emoji_name=None):
        """
        Log a WARNING level message with an optional emoji.
        
        Args:
            message (str): The message to log
            emoji_name (str, optional): Name of the emoji to prepend
        """
        self.log(logging.WARNING, message, emoji_name)
    
    def error(self, message, emoji_name=None):
        """
        Log an ERROR level message with an optional emoji.
        
        Args:
            message (str): The message to log
            emoji_name (str, optional): Name of the emoji to prepend
        """
        self.log(logging.ERROR, message, emoji_name)