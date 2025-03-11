import logging
import pytest
import sys
from src.stack_trace_logger import log_stack_trace

class MockLogger:
    def __init__(self):
        self.logged_messages = []
        self.logged_levels = []

    def log(self, level, msg):
        self.logged_messages.append(msg)
        self.logged_levels.append(level)

def test_log_stack_trace_with_no_exception():
    """Test logging current stack trace"""
    mock_logger = MockLogger()
    
    stack_trace = log_stack_trace(logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.ERROR
    assert 'test_log_stack_trace_with_no_exception' in stack_trace

def test_log_stack_trace_with_exception():
    """Test logging an explicit exception"""
    mock_logger = MockLogger()
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        stack_trace = log_stack_trace(e, logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.ERROR
    assert 'ValueError: Test exception' in stack_trace

def test_log_stack_trace_custom_log_level():
    """Test logging with a custom log level"""
    mock_logger = MockLogger()
    
    stack_trace = log_stack_trace(
        logger=mock_logger, 
        log_level=logging.WARNING
    )
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.WARNING

def test_log_stack_trace_returns_string():
    """Verify that the function returns a string"""
    mock_logger = MockLogger()
    
    stack_trace = log_stack_trace(logger=mock_logger)
    
    assert isinstance(stack_trace, str)
    assert len(stack_trace) > 0