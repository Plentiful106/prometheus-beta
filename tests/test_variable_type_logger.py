import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Test with different types of variables
    test_cases = [
        (42, 'int'),
        ('hello', 'str'),
        (3.14, 'float'),
        ([1, 2, 3], 'list'),
        ({'a': 1}, 'dict'),
        ((1, 2), 'tuple'),
        (None, 'NoneType'),
        (True, 'bool')
    ]

    for var, expected_type in test_cases:
        # Capture the returned type and the log output
        returned_type = log_variable_type(var)
        
        # Check if returned type matches expected type
        assert returned_type == expected_type
        
        # Check if log message contains the type
        log_output = log_capture.getvalue()
        assert f"Variable type: {expected_type}" in log_output
        
        # Clear the log capture for next iteration
        log_capture.truncate(0)
        log_capture.seek(0)

def test_log_variable_type_custom_object():
    # Test with a custom class
    class CustomClass:
        pass
    
    custom_obj = CustomClass()
    
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Log the type
    returned_type = log_variable_type(custom_obj)
    
    # Check if returned type is 'CustomClass'
    assert returned_type == 'CustomClass'
    
    # Check if log message contains the type
    log_output = log_capture.getvalue()
    assert "Variable type: CustomClass" in log_output