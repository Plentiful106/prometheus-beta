from typing import List

def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers in the input list.
    
    Args:
        numbers (List[int]): A list of integers to check for duplicates.
    
    Returns:
        List[int]: A list of integers that appear more than once in the input list.
    
    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
        [2, 3]
        >>> find_duplicates([1, 2, 3, 4, 5])
        []
        >>> find_duplicates([])
        []
    """
    # Use a set to track seen numbers and duplicates
    seen = set()
    duplicates = set()
    
    # Iterate through the list to find duplicates
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # Convert duplicates to a sorted list for consistent output
    return sorted(list(duplicates))