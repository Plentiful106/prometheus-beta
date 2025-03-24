import os
import json
import pytest
from datetime import datetime
import sys
import tempfile

# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_logger import log_with_timestamp

def test_log_with_timestamp_basic():
    """Test basic logging functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'log.json')
        
        # Log a simple string
        log_with_timestamp("Test log message", log_file)
        
        # Verify log file contents
        with open(log_file, 'r') as f:
            logs = json.load(f)
        
        assert len(logs) == 1
        assert 'timestamp' in logs[0]
        assert 'data' in logs[0]
        assert logs[0]['data'] == "Test log message"
        assert datetime.fromisoformat(logs[0]['timestamp'])  # Validate timestamp format

def test_log_multiple_entries():
    """Test logging multiple entries"""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'log.json')
        
        # Log multiple different types of data
        log_with_timestamp("First message", log_file)
        log_with_timestamp(42, log_file)
        log_with_timestamp({"key": "value"}, log_file)
        
        # Verify log file contents
        with open(log_file, 'r') as f:
            logs = json.load(f)
        
        assert len(logs) == 3
        assert logs[0]['data'] == "First message"
        assert logs[1]['data'] == 42
        assert logs[2]['data'] == {"key": "value"}

def test_log_creates_directory():
    """Test that log function creates directory if it doesn't exist"""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'nested', 'directory', 'log.json')
        
        log_with_timestamp("Test log", log_file)
        
        assert os.path.exists(log_file)

def test_log_handles_existing_file():
    """Test logging to an existing file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'log.json')
        
        # Manually create initial file
        with open(log_file, 'w') as f:
            json.dump([{"existing": "entry"}], f)
        
        log_with_timestamp("New message", log_file)
        
        # Verify log file contents
        with open(log_file, 'r') as f:
            logs = json.load(f)
        
        assert len(logs) == 2
        assert logs[0]['existing'] == "entry"
        assert logs[1]['data'] == "New message"

def test_log_handles_empty_or_invalid_file():
    """Test logging to an empty or invalid JSON file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Empty file
        log_file_empty = os.path.join(tmpdir, 'empty_log.json')
        with open(log_file_empty, 'w') as f:
            f.write('')
        
        log_with_timestamp("Message to empty file", log_file_empty)
        
        # Invalid JSON file
        log_file_invalid = os.path.join(tmpdir, 'invalid_log.json')
        with open(log_file_invalid, 'w') as f:
            f.write('Not a valid JSON')
        
        log_with_timestamp("Message to invalid file", log_file_invalid)
        
        # Verify both logs were created successfully
        with open(log_file_empty, 'r') as f:
            logs_empty = json.load(f)
        
        with open(log_file_invalid, 'r') as f:
            logs_invalid = json.load(f)
        
        assert len(logs_empty) == 1
        assert len(logs_invalid) == 1
        assert logs_empty[0]['data'] == "Message to empty file"
        assert logs_invalid[0]['data'] == "Message to invalid file"

def test_log_unsupported_type():
    """Test logging an unsupported (non-JSON-serializable) type"""
    with tempfile.TemporaryDirectory() as tmpdir:
        log_file = os.path.join(tmpdir, 'log.json')
        
        # Test with a function (non-serializable)
        with pytest.raises(TypeError):
            log_with_timestamp(lambda x: x, log_file)