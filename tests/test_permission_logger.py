import pytest
import logging
from src.permission_logger import PermissionLogger, UserRole

class TestPermissionLogger:
    @pytest.fixture
    def logger(self):
        """Create a fresh PermissionLogger for each test."""
        return PermissionLogger()

    def test_log_with_default_role(self, logger, caplog):
        """Test logging message with default user role."""
        caplog.set_level(logging.INFO)
        result = logger.log("Test message")
        assert result is True
        assert "Test message" in caplog.text

    def test_log_with_different_levels(self, logger, caplog):
        """Test logging messages at different levels."""
        levels = [
            (logging.DEBUG, "Debug message"),
            (logging.INFO, "Info message"),
            (logging.WARNING, "Warning message"),
            (logging.ERROR, "Error message"),
            (logging.CRITICAL, "Critical message")
        ]

        for level, message in levels:
            caplog.clear()
            caplog.set_level(level)
            result = logger.log(message, level=level)
            assert result is True
            assert message in caplog.text

    def test_log_with_high_min_role(self, logger, caplog):
        """Test logging message requiring higher role."""
        result = logger.log("Admin message", min_role=UserRole.ADMIN)
        assert result is False
        assert len(caplog.records) == 0

    def test_invalid_message_type(self, logger):
        """Test logging with invalid message type."""
        with pytest.raises(ValueError, match="Message must be a string"):
            logger.log(123)

    def test_invalid_logging_level(self, logger):
        """Test logging with invalid logging level."""
        with pytest.raises(ValueError, match="Invalid logging level"):
            logger.log("Test", level=999)

    def test_invalid_user_role(self, logger):
        """Test logging with invalid user role."""
        with pytest.raises(ValueError, match="Invalid user role"):
            logger.log("Test", min_role=999)

    def test_log_edge_cases(self, logger, caplog):
        """Test edge cases for logging."""
        # Empty string
        result = logger.log("")
        assert result is True
        
        # Long message
        long_message = "x" * 1000
        result = logger.log(long_message)
        assert result is True
        assert long_message in caplog.text