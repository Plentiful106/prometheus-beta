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

def test_log_query_time_successful_query(caplog):
    # Setup log capture
    caplog.set_level(logging.INFO)
    
    # Perform query
    db = MockDatabase()
    result = db.successful_query(0.05)
    
    # Check result
    assert result == "Query successful"
    
    # Check log message
    log_records = [record.message for record in caplog.records]
    assert any("Query 'successful_query' executed in" in msg for msg in log_records)
    assert any("ms" in msg for msg in log_records)

def test_log_query_time_error_handling(caplog):
    # Setup log capture
    caplog.set_level(logging.ERROR)
    
    # Perform query and expect error
    db = MockDatabase()
    with pytest.raises(ValueError, match="Simulated query error"):
        db.query_with_error()
    
    # Check error log message
    log_records = [record.message for record in caplog.records]
    assert any("Error in query 'query_with_error'" in msg for msg in log_records)

def test_log_query_time_invalid_input():
    with pytest.raises(TypeError, match="Decorated object must be a callable function"):
        log_query_time("not a function")