import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_standard_conversion():
    """Test conversion of standard temperatures."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_decimal_conversion():
    """Test conversion with decimal temperatures."""
    assert round(celsius_to_fahrenheit(37.5), 2) == 99.5
    assert round(celsius_to_fahrenheit(-17.8), 2) == 0

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([])

def test_large_numbers():
    """Test conversion with large number inputs."""
    assert round(celsius_to_fahrenheit(1000), 2) == 1832
    assert round(celsius_to_fahrenheit(-1000), 2) == -1768