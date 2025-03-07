import pytest
import time
import logging
from src.execution_timer import log_execution_time

# Configure a test logger
class TestLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_basic():
    # Create a test logger
    test_logger = TestLogger()
    
    # Create a test function with the decorator
    @log_execution_time(logger=test_logger)
    def test_func():
        time.sleep(0.1)  # Simulate some work
    
    # Call the function
    test_func()
    
    # Check that a log was recorded
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    
    # Verify log details
    assert log_type == 'info'
    assert 'test_func' in log_message
    assert 'executed in' in log_message

def test_log_execution_time_with_args():
    # Create a test logger
    test_logger = TestLogger()
    
    # Create a test function with arguments
    @log_execution_time(logger=test_logger)
    def test_func_with_args(a, b):
        time.sleep(0.05)
        return a + b
    
    # Call the function
    result = test_func_with_args(3, 4)
    
    # Check function return value
    assert result == 7
    
    # Check that a log was recorded
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    
    # Verify log details
    assert log_type == 'info'
    assert 'test_func_with_args' in log_message

def test_log_execution_time_exception():
    # Create a test logger
    test_logger = TestLogger()
    
    # Create a function that raises an exception
    @log_execution_time(logger=test_logger)
    def test_func_with_error():
        raise ValueError("Test error")
    
    # Check that the exception is re-raised
    with pytest.raises(ValueError, match="Test error"):
        test_func_with_error()
    
    # Check that an error log was recorded
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    
    # Verify log details
    assert log_type == 'error'
    assert 'Test error' in log_message