"""
Custom logging module with styling capabilities.

This module provides a flexible logging function that allows custom 
styling of log messages.
"""

import sys
from typing import Optional, Union, TextIO


def log_message(
    message: str, 
    color: Optional[str] = None, 
    bold: bool = False, 
    italic: bool = False, 
    underline: bool = False, 
    output: TextIO = sys.stdout
) -> None:
    """
    Log a message with optional custom styling.

    Args:
        message (str): The message to log
        color (Optional[str], optional): Color of the text. 
            Supports: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'. 
            Defaults to None (no color).
        bold (bool, optional): Make text bold. Defaults to False.
        italic (bool, optional): Make text italic. Defaults to False.
        underline (bool, optional): Underline the text. Defaults to False.
        output (TextIO, optional): Output stream to write to. Defaults to sys.stdout.

    Raises:
        ValueError: If an unsupported color is provided.
    """
    # ANSI color codes
    colors = {
        'red': '\033[31m',
        'green': '\033[32m', 
        'yellow': '\033[33m',
        'blue': '\033[34m', 
        'magenta': '\033[35m',
        'cyan': '\033[36m', 
        'white': '\033[37m'
    }

    # ANSI text styling codes
    style_codes = []
    
    # Add color if specified
    if color:
        if color.lower() not in colors:
            raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(colors.keys())}")
        style_codes.append(colors[color.lower()])
    
    # Add additional text styles
    if bold:
        style_codes.append('\033[1m')
    if italic:
        style_codes.append('\033[3m')
    if underline:
        style_codes.append('\033[4m')

    # Reset code to clear all styling after the message
    reset_code = '\033[0m'

    # Combine styling and message only if there are styling codes
    if style_codes:
        styled_message = ''.join(style_codes) + message + reset_code
        print(styled_message, file=output)
    else:
        print(message, file=output)