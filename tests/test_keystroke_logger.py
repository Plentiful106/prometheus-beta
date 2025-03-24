import os
import tempfile
import pytest
import logging
import threading
import time
from src.keystroke_logger import KeystrokeLogger

class TestKeystrokeLogger:
    def setup_method(self):
        """
        Setup method to create a new KeystrokeLogger for each test.
        """
        # Use a temporary file for logging
        temp_dir = tempfile.gettempdir()
        self.log_file = os.path.join(temp_dir, 'test_keystrokes.log')
        self.logger = KeystrokeLogger(log_file=self.log_file)

    def teardown_method(self):
        """
        Cleanup method to stop logging and remove log file after each test.
        """
        self.logger.stop_logging()
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_single_keystroke(self):
        """
        Test logging a single keystroke.
        """
        self.logger.start_logging()
        self.logger.log_keystroke('a')
        time.sleep(0.2)  # Allow time for logging
        self.logger.stop_logging()

        with open(self.log_file, 'r') as f:
            log_content = f.read()
            assert 'Keystroke: a' in log_content

    def test_log_multiple_keystrokes(self):
        """
        Test logging multiple keystrokes.
        """
        self.logger.start_logging()
        test_keys = ['h', 'e', 'l', 'l', 'o']
        for key in test_keys:
            self.logger.log_keystroke(key)
        time.sleep(0.2)  # Allow time for logging
        self.logger.stop_logging()

        with open(self.log_file, 'r') as f:
            log_content = f.read()
            for key in test_keys:
                assert f'Keystroke: {key}' in log_content

    def test_invalid_keystroke(self):
        """
        Test that logging invalid keystrokes raises a ValueError.
        """
        with pytest.raises(ValueError):
            self.logger.log_keystroke('')  # Empty string
        
        with pytest.raises(ValueError):
            self.logger.log_keystroke('ab')  # Multi-character string

    def test_start_stop_logging(self):
        """
        Test starting and stopping the logging process.
        """
        self.logger.start_logging()
        assert self.logger._log_thread is not None
        assert self.logger._log_thread.is_alive()

        self.logger.stop_logging()
        time.sleep(0.1)
        assert not self.logger._log_thread.is_alive()

    def test_multiple_start_calls(self):
        """
        Test that multiple start calls do not create multiple threads.
        """
        self.logger.start_logging()
        first_thread = self.logger._log_thread

        self.logger.start_logging()
        second_thread = self.logger._log_thread

        assert first_thread == second_thread