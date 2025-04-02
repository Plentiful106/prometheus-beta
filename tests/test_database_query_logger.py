import pytest
import time
import logging
from src.database_query_logger import log_query_time

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def handler(self, record):
        self.log_messages.append(record.getMessage())

# Mock database query functions for testing
class MockDatabase:
    @log_query_time
    def successful_query(self, delay=0.01):
        time.sleep(delay)
        return "Query successful"
    
    @log_query_time
    def query_with_error(self):
        raise ValueError("Simulated query error")

def test_log_query_time_successful_query():
    # Setup log capture
    log_capture = LogCapture()
    logger = logging.getLogger()
    handler = logging.Handler()
    handler.emit = log_capture.handler
    logger.addHandler(handler)
    
    # Perform query
    db = MockDatabase()
    result = db.successful_query(0.05)
    
    # Check result
    assert result == "Query successful"
    
    # Check log message
    assert len(log_capture.log_messages) > 0
    log_message = log_capture.log_messages[-1]
    assert "Query 'successful_query' executed in" in log_message
    assert "ms" in log_message
    
    # Cleanup
    logger.removeHandler(handler)

def test_log_query_time_error_handling():
    # Setup log capture
    log_capture = LogCapture()
    logger = logging.getLogger()
    handler = logging.Handler()
    handler.emit = log_capture.handler
    logger.addHandler(handler)
    
    # Perform query and expect error
    db = MockDatabase()
    with pytest.raises(ValueError, match="Simulated query error"):
        db.query_with_error()
    
    # Check error log message
    assert len(log_capture.log_messages) > 0
    log_message = log_capture.log_messages[-1]
    assert "Error in query 'query_with_error'" in log_message
    
    # Cleanup
    logger.removeHandler(handler)

def test_log_query_time_invalid_input():
    with pytest.raises(TypeError):
        log_query_time("not a function")