import logging
import pytest
from src.debug_logger import conditional_debug_log

class TestConditionalDebugLogger:
    def test_debug_logging_enabled(self, caplog):
        # Setup logging
        caplog.set_level(logging.DEBUG)
        logger = logging.getLogger()

        # Create a test function with debug logging
        @conditional_debug_log(condition=True, logger=logger)
        def sample_function(x, y):
            return x + y

        # Call the function and check logging
        result = sample_function(3, 4)
        assert result == 7

        # Check log messages
        log_records = caplog.records
        assert len(log_records) == 2
        
        # Check input logging
        assert "Calling sample_function with args: (3, 4), kwargs: {}" in log_records[0].message
        # Check return value logging
        assert "sample_function returned: 7" in log_records[1].message

    def test_debug_logging_disabled(self, caplog):
        # Setup logging
        caplog.set_level(logging.DEBUG)
        logger = logging.getLogger()

        # Create a test function with debug logging disabled
        @conditional_debug_log(condition=False, logger=logger)
        def sample_function(x, y):
            return x + y

        # Call the function and check no logging occurred
        result = sample_function(3, 4)
        assert result == 7

        # Ensure no log records were created
        assert len(caplog.records) == 0

    def test_default_logger(self, caplog):
        # Setup logging
        caplog.set_level(logging.DEBUG)

        # Create a test function with default logger
        @conditional_debug_log()
        def sample_function(x, y):
            return x + y

        # Call the function and check logging
        result = sample_function(3, 4)
        assert result == 7

        # Check log messages
        log_records = caplog.records
        assert len(log_records) == 2
        
        # Check input logging
        assert "Calling sample_function with args: (3, 4), kwargs: {}" in log_records[0].message
        # Check return value logging
        assert "sample_function returned: 7" in log_records[1].message

    def test_function_metadata_preserved(self):
        # Test that function metadata is preserved
        @conditional_debug_log()
        def sample_function(x, y):
            """A sample function for testing."""
            return x + y

        assert sample_function.__name__ == 'sample_function'
        assert sample_function.__doc__ == 'A sample function for testing.'