def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort (Bead Sort) algorithm.
    
    Spaghetti Sort is a unique sorting algorithm that works by visualizing 
    the sorting process as beads sliding down vertical rods.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains negative numbers.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-negative integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum value to determine the number of rods
    max_val = max(arr)
    
    # Create the "rods" representation
    rods = [0] * (max_val + 1)
    
    # Place beads on rods
    for num in arr:
        rods[num] += 1
    
    # Collect sorted values
    sorted_arr = []
    for height, count in enumerate(rods):
        sorted_arr.extend([height] * count)
    
    return sorted_arr