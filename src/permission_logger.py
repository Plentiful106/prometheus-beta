import logging
from typing import Optional, Union

class UserRole:
    """Enum-like class representing user roles and their permission levels."""
    ADMIN = 3
    MANAGER = 2
    USER = 1
    GUEST = 0

class PermissionLogger:
    """
    A logger that controls message logging based on user permissions.
    
    Supports different logging levels based on user roles.
    """
    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize the PermissionLogger.
        
        Args:
            log_level (int, optional): Base logging level. Defaults to logging.INFO.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        # Create console handler if not already exists
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def log(self, message: str, min_role: int = UserRole.USER, level: int = logging.INFO) -> bool:
        """
        Log a message if the user's role meets the minimum permission requirement.
        
        Args:
            message (str): The message to log
            min_role (int, optional): Minimum role required to log. Defaults to UserRole.USER.
            level (int, optional): Logging level. Defaults to logging.INFO.
        
        Returns:
            bool: True if message was logged, False otherwise
        
        Raises:
            ValueError: If an invalid role or logging level is provided
        """
        # Validate inputs
        if not isinstance(message, str):
            raise ValueError("Message must be a string")
        
        if level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            raise ValueError(f"Invalid logging level: {level}")
        
        if min_role not in [UserRole.GUEST, UserRole.USER, UserRole.MANAGER, UserRole.ADMIN]:
            raise ValueError(f"Invalid user role: {min_role}")
        
        # Check if current user role can log this message
        current_user_role = self._get_current_user_role()
        
        if current_user_role >= min_role:
            # Log the message at the specified level
            if level == logging.DEBUG:
                self.logger.debug(message)
            elif level == logging.INFO:
                self.logger.info(message)
            elif level == logging.WARNING:
                self.logger.warning(message)
            elif level == logging.ERROR:
                self.logger.error(message)
            elif level == logging.CRITICAL:
                self.logger.critical(message)
            
            return True
        
        return False

    def _get_current_user_role(self) -> int:
        """
        Simulate getting current user's role.
        
        In a real-world scenario, this would interact with authentication/authorization system.
        
        Returns:
            int: Current user's role (defaults to USER)
        """
        # TODO: Implement actual user role retrieval mechanism
        return UserRole.USER