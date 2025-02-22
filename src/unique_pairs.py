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
    
    # Generate all unique pairs
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Ensure pairs are sorted to prevent duplicates like (1,2) and (2,1)
            pair = tuple(sorted((numbers[i], numbers[j])))
            unique_pairs.add(pair)
    
    return list(unique_pairs)