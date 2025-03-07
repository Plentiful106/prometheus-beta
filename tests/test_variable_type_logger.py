import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type(capsys):
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
        # Log the type
        returned_type = log_variable_type(var)
        
        # Capture the output
        captured = capsys.readouterr()
        
        # Check if returned type matches expected type
        assert returned_type == expected_type
        
        # Check if log output contains the type
        assert f"Variable type: {expected_type}" in captured.err

def test_log_variable_type_custom_object(capsys):
    # Test with a custom class
    class CustomClass:
        pass
    
    custom_obj = CustomClass()
    
    # Log the type
    returned_type = log_variable_type(custom_obj)
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check if returned type is 'CustomClass'
    assert returned_type == 'CustomClass'
    
    # Check if log output contains the type
    assert "Variable type: CustomClass" in captured.err