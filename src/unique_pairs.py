def get_unique_pairs(numbers):
    """
    Returns all unique pairs of elements from a given list of integers.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of unique pairs (tuples) of elements from the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Use set to ensure uniqueness and prevent duplicate pairs
    unique_pairs = set()
    
    # Use set of unique numbers to remove duplicates
    unique_numbers = list(set(numbers))
    
    # Generate all unique pairs
    for i in range(len(unique_numbers)):
        for j in range(i+1, len(unique_numbers)):
            # Ensure pairs are sorted to prevent duplicates like (1,2) and (2,1)
            pair = tuple(sorted((unique_numbers[i], unique_numbers[j])))
            unique_pairs.add(pair)
    
    return list(unique_pairs)