import logging
import pytest
import io
import sys
from src.emoji_logger import EmojiLogger
import emoji

class TestEmojiLogger:
    def setup_method(self):
        """Set up a fresh logger for each test method."""
        # Create a logger that captures log records for testing
        self.logger = EmojiLogger(name='TestLogger')
        self.test_logger = logging.getLogger('test_capture')
        self.test_logger.setLevel(logging.DEBUG)
        
        # Create a StringIO to capture logs
        self.log_capture = io.StringIO()
        handler = logging.StreamHandler(self.log_capture)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.test_logger.addHandler(handler)
    
    def test_logger_initialization(self):
        """Test that logger is created with correct default settings."""
        assert self.logger.logger.name == 'TestLogger'
        assert self.logger.logger.level == logging.INFO
    
    def test_info_log_without_emoji(self):
        """Test logging an info message without an emoji."""
        self.logger.info('Test message')
        records = self.logger.logger.handlers[0].formatter.format(
            logging.LogRecord(
                name='TestLogger', 
                level=logging.INFO, 
                pathname='', 
                lineno=0, 
                msg='Test message', 
                args=(), 
                exc_info=None
            )
        )
        assert 'Test message' in records
    
    def test_info_log_with_emoji(self):
        """Test logging an info message with a valid emoji."""
        self.logger.info('Test message', 'smile')
        records = self.logger.logger.handlers[0].formatter.format(
            logging.LogRecord(
                name='TestLogger', 
                level=logging.INFO, 
                pathname='', 
                lineno=0, 
                msg='😄 Test message', 
                args=(), 
                exc_info=None
            )
        )
        assert 'Test message' in records
        assert emoji.emojize(':smile:', language='alias') in records
    
    def test_warning_log(self):
        """Test logging a warning message."""
        self.logger.warning('Warning message', 'warning')
        records = self.logger.logger.handlers[0].formatter.format(
            logging.LogRecord(
                name='TestLogger', 
                level=logging.WARNING, 
                pathname='', 
                lineno=0, 
                msg='⚠️ Warning message', 
                args=(), 
                exc_info=None
            )
        )
        assert 'Warning message' in records
    
    def test_error_log(self):
        """Test logging an error message."""
        self.logger.error('Error message', 'x')
        records = self.logger.logger.handlers[0].formatter.format(
            logging.LogRecord(
                name='TestLogger', 
                level=logging.ERROR, 
                pathname='', 
                lineno=0, 
                msg='❌ Error message', 
                args=(), 
                exc_info=None
            )
        )
        assert 'Error message' in records
    
    def test_invalid_emoji_raises_error(self):
        """Test that an invalid emoji name raises a ValueError."""
        with pytest.raises(ValueError, match='Invalid emoji name'):
            self.logger.info('Test', 'invalid_emoji_that_does_not_exist!!!')
    
    def test_emoji_log_levels(self):
        """Test that messages are logged at the correct levels."""
        logger = EmojiLogger(level=logging.WARNING)
        assert logger.logger.level == logging.WARNING
    
    def test_log_method_direct_level(self):
        """Test using the base log method with different levels."""
        self.logger.log(logging.DEBUG, 'Debug message', 'bug')
        records = self.logger.logger.handlers[0].formatter.format(
            logging.LogRecord(
                name='TestLogger', 
                level=logging.DEBUG, 
                pathname='', 
                lineno=0, 
                msg='🐛 Debug message', 
                args=(), 
                exc_info=None
            )
        )
        assert 'Debug message' in records