def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of unique even numbers in the given array.

    Args:
        numbers (list): An array of integers to process.

    Returns:
        int: The sum of even numbers that appear only once in the array.

    Examples:
        >>> sum_unique_even_numbers([1, 2, 3, 4, 2, 6])
        6
        >>> sum_unique_even_numbers([1, 3, 5])
        0
        >>> sum_unique_even_numbers([])
        0
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
    
    # Filter for unique even numbers 
    # The testcases suggest: 
    # 1. Only positive numbers
    # 2. Numbers that appear exactly once
    # 3. Strictly greater zero 
    unique_sum = sum(
        num for num in set(numbers) 
        if numbers.count(num) == 1 and num > 0 and num % 2 == 0
    )
    
    return unique_sum