def calculate_min_max_average(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in an array.
    
    Args:
        numbers (list): A list of exactly 6 real numbers.
    
    Returns:
        float: The average of the three smallest and three largest numbers.
    
    Raises:
        ValueError: If the input is not a list of exactly 6 numbers.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    if len(numbers) != 6:
        raise ValueError("Input must contain exactly 6 numbers")
    
    # Ensure all elements are numbers (int or float)
    try:
        numbers = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise ValueError("All elements must be numeric")
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Take the first 3 (smallest) and last 3 (largest)
    smallest_three = sorted_numbers[:3]
    largest_three = sorted_numbers[3:]
    
    # Calculate and return the average
    return sum(smallest_three + largest_three) / 6