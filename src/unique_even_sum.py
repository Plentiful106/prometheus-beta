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
    
    # Count the occurrences of each unique even number
    even_counts = {}
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    
    # Sum the unique even numbers (those with exactly one occurrence)
    unique_even_sum = sum(
        num for num, count in even_counts.items() 
        if count == 1
    )
    
    return unique_even_sum