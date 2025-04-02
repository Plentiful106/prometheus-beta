import math

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The standard deviation of the input list.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric values.
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Validate input is numeric using isinstance instead of float conversion
    def is_numeric(x):
        return isinstance(x, (int, float))
    
    # Check if all elements are numeric
    if not all(is_numeric(x) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Convert to float to ensure precision
    numbers = [float(x) for x in numbers]
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate sample standard deviation (using n-1 in denominator)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    
    # Return square root of variance (standard deviation)
    return math.sqrt(variance)