def compute_weighted_sum(numbers, weights):
    """
    Compute the total weighted sum of a list of numbers using their corresponding weights.
    
    Args:
        numbers (list): A list of numeric values to be weighted.
        weights (list): A list of weights corresponding to the numbers.
    
    Returns:
        float: The total weighted sum.
    
    Raises:
        ValueError: If the lengths of numbers and weights lists do not match,
                    if either list is empty, or if lists contain non-numeric values.
        TypeError: If input is not a list or contains non-numeric values.
    """
    # Input validation
    if not isinstance(numbers, list) or not isinstance(weights, list):
        raise TypeError("Inputs must be lists")
    
    # Check for empty lists
    if len(numbers) == 0 or len(weights) == 0:
        raise ValueError("Input lists cannot be empty")
    
    # Check for length mismatch
    if len(numbers) != len(weights):
        raise ValueError("Numbers and weights lists must have equal length")
    
    # Validate numeric inputs
    try:
        numbers = [float(num) for num in numbers]
        weights = [float(weight) for weight in weights]
    except (TypeError, ValueError):
        raise TypeError("All elements must be numeric")
    
    # Compute weighted sum
    return sum(num * weight for num, weight in zip(numbers, weights))