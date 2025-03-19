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
    
    # Use a list to track unique even numbers
    unique_evens = []
    seen_numbers = {}
    
    for num in numbers:
        if num in seen_numbers:
            # If we've seen this number before, remove it from unique_evens if it was there
            if num in unique_evens:
                unique_evens.remove(num)
        else:
            # First time seeing this number
            seen_numbers[num] = 1
            if num > 0 and num % 2 == 0:
                unique_evens.append(num)
    
    return sum(unique_evens)