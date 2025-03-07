import pytest
import logging
from src.input_validation_logger import log_validation_message

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.records = []
    
    def handler(self, record):
        self.records.append(record)

@pytest.fixture
def log_capture():
    """Fixture to capture log messages"""
    capture = LogCapture()
    logger = logging.getLogger()
    logger.addHandler(logging.Handler())
    logger.handlers[-1].emit = capture.handler
    return capture

@log_validation_message()
def example_function(arg1, arg2=None):
    return arg1, arg2

def test_log_validation_none_args(log_capture):
    """Test logging when arguments are None"""
    result = example_function(10, None)
    
    # Check the function still works
    assert result == (10, None)
    
    # Check log messages
    assert len(log_capture.records) == 1
    record = log_capture.records[0]
    assert record.levelno == logging.WARNING
    assert "arg2 is None" in record.getMessage()

def test_log_validation_empty_args(log_capture):
    """Test logging when arguments are empty/falsy"""
    result = example_function(10, [])
    
    # Check the function still works
    assert result == (10, [])
    
    # Check log messages
    assert len(log_capture.records) == 1
    record = log_capture.records[0]
    assert record.levelno == logging.WARNING
    assert "arg2 is empty/falsy" in record.getMessage()

def test_different_severity_levels():
    """Test different logging severity levels"""
    @log_validation_message(severity='error')
    def error_level_func(arg=None):
        return arg
    
    with pytest.raises(ValueError):
        log_validation_message(severity='invalid_level')
    
    # This should not raise an error
    log_validation_message(severity='debug')
    log_validation_message(severity='info')
    log_validation_message(severity='warning')
    log_validation_message(severity='error')
    log_validation_message(severity='critical')

def test_decorator_preserves_function_metadata():
    """Ensure the decorator preserves function metadata"""
    @log_validation_message()
    def test_func(x, y):
        """Docstring for test function"""
        return x + y
    
    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'Docstring for test function'