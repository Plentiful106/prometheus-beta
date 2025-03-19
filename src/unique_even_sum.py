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
    
    # Count occurrences of each number
    number_counts = {}
    for num in numbers:
        # Validate each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        number_counts[num] = number_counts.get(num, 0) + 1
    
    # Sum unique even numbers
    unique_even_sum = sum(
        num for num in number_counts 
        if abs(num) % 2 == 0 and number_counts[num] == 1
    )
    
    return unique_even_sum