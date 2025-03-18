import logging
import pytest
import io
import sys
from src.emoji_logger import EmojiLogger
import emoji

class TestEmojiLogger:
    def setup_method(self):
        """Set up a fresh logger for each test method."""
        self.logger = EmojiLogger(name='TestLogger')
        
        # Capture stdout for testing log output
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output
    
    def teardown_method(self):
        """Reset stdout after each test."""
        sys.stdout = sys.__stdout__
    
    def test_logger_initialization(self):
        """Test that logger is created with correct default settings."""
        assert self.logger.logger.name == 'TestLogger'
        assert self.logger.logger.level == logging.INFO
    
    def test_info_log_without_emoji(self):
        """Test logging an info message without an emoji."""
        self.logger.info('Test message')
        output = self.captured_output.getvalue()
        assert 'Test message' in output
        assert ' - INFO - ' in output
    
    def test_info_log_with_emoji(self):
        """Test logging an info message with a valid emoji."""
        self.logger.info('Test message', 'smile')
        output = self.captured_output.getvalue()
        assert 'Test message' in output
        assert emoji.emojize(':smile:', language='alias') in output
    
    def test_warning_log(self):
        """Test logging a warning message."""
        self.logger.warning('Warning message', 'warning')
        output = self.captured_output.getvalue()
        assert 'Warning message' in output
        assert ' - WARNING - ' in output
    
    def test_error_log(self):
        """Test logging an error message."""
        self.logger.error('Error message', 'x')
        output = self.captured_output.getvalue()
        assert 'Error message' in output
        assert ' - ERROR - ' in output
    
    def test_invalid_emoji_raises_error(self):
        """Test that an invalid emoji name raises a ValueError."""
        with pytest.raises(ValueError, match='Invalid emoji name'):
            self.logger.info('Test', 'invalid_emoji_that_does_not_exist')
    
    def test_emoji_log_levels(self):
        """Test that messages are logged at the correct levels."""
        logger = EmojiLogger(level=logging.WARNING)
        assert logger.logger.level == logging.WARNING
    
    def test_log_method_direct_level(self):
        """Test using the base log method with different levels."""
        self.logger.log(logging.DEBUG, 'Debug message', 'bug')
        output = self.captured_output.getvalue()
        assert 'Debug message' in output