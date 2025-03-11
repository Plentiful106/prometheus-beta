import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

def test_readline_logger_basic_initialization():
    """Test basic initialization of ReadlineLogger."""
    logger = ReadlineLogger()
    assert logger._logger is not None
    assert logger._logger.level == logging.INFO

def test_readline_logger_custom_logger():
    """Test initialization with a custom logger."""
    custom_logger = logging.getLogger('test_logger')
    custom_logger.setLevel(logging.DEBUG)
    
    logger = ReadlineLogger(logger=custom_logger, log_level=logging.DEBUG)
    assert logger._logger == custom_logger
    assert logger._logger.level == logging.DEBUG

def test_readline_logger_input_logging():
    """Test logging of input prompts."""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    
    readline_logger = ReadlineLogger(logger=logger)
    
    # Simulate user input
    with patch('builtins.input', return_value='test input'):
        result = readline_logger.log_input("Enter something: ")
    
    log_output = log_capture.getvalue()
    
    assert "Prompt: Enter something: " in log_output
    assert "Input received: test input" in log_output
    assert result == "test input"

def test_readline_logger_input_validation():
    """Test input validation with custom validator."""
    def validate_positive_number(value):
        """Validate that input is a positive number."""
        try:
            num = float(value)
            return num > 0
        except ValueError:
            return False
    
    readline_logger = ReadlineLogger()
    
    # Successful validation
    with patch('builtins.input', return_value='42'):
        result = readline_logger.log_input("Enter a positive number: ", 
                                           validator=validate_positive_number)
        assert result == '42'
    
    # Failed validation scenarios
    with patch('builtins.input', side_effect=['-5', 'invalid', '10']):
        with patch.object(readline_logger._logger, 'warning') as mock_warning, \
             patch.object(readline_logger._logger, 'error') as mock_error:
            result = readline_logger.log_input("Enter a positive number: ", 
                                               validator=validate_positive_number)
            assert result == '10'
            assert mock_warning.call_count >= 2
            assert mock_error.call_count >= 2

def test_readline_logger_error_handling():
    """Test error handling during input."""
    readline_logger = ReadlineLogger()
    
    # Test unexpected error handling
    with patch('builtins.input', side_effect=Exception("Unexpected error")):
        with pytest.raises(Exception):
            readline_logger.log_input("Enter something: ")

# Optional: Performance and edge case tests
def test_readline_logger_long_input():
    """Test handling of very long inputs."""
    readline_logger = ReadlineLogger()
    
    long_input = "x" * 10000  # Very long input
    with patch('builtins.input', return_value=long_input):
        result = readline_logger.log_input("Enter a long string: ")
        assert result == long_input