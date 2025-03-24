import sys
import threading
import queue
import logging

class KeystrokeLogger:
    """
    A class to log keystrokes entered by the user.
    
    This logger provides basic functionality to capture and log keystrokes
    with thread-safe logging mechanisms.
    """
    
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'keystrokes.log'.
        """
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Queue to manage keystrokes
        self.keystroke_queue = queue.Queue()
        
        # Flag to control logging thread
        self._stop_logging = threading.Event()
        
        # Logging thread
        self._log_thread = None

    def start_logging(self):
        """
        Start the keystroke logging process.
        
        Begins a background thread to continuously log keystrokes.
        """
        if self._log_thread and self._log_thread.is_alive():
            return  # Already logging
        
        self._stop_logging.clear()
        self._log_thread = threading.Thread(target=self._log_keystrokes)
        self._log_thread.daemon = True
        self._log_thread.start()

    def stop_logging(self):
        """
        Stop the keystroke logging process.
        
        Signals the logging thread to stop and waits for it to terminate.
        """
        if not self._log_thread:
            return
        
        self._stop_logging.set()
        if self._log_thread.is_alive():
            self._log_thread.join()

    def log_keystroke(self, key):
        """
        Add a keystroke to the logging queue.
        
        Args:
            key (str): The keystroke to be logged.
        
        Raises:
            ValueError: If the input is not a single character.
        """
        if not isinstance(key, str) or len(key) != 1:
            raise ValueError("Keystroke must be a single character")
        
        self.keystroke_queue.put(key)

    def _log_keystrokes(self):
        """
        Internal method to process and log keystrokes from the queue.
        Runs in a separate thread.
        """
        while not self._stop_logging.is_set():
            try:
                # Use a timeout to allow checking the stop flag
                key = self.keystroke_queue.get(timeout=0.1)
                self.logger.info(f"Keystroke: {key}")
            except queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Error logging keystroke: {e}")