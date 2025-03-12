def gravity_sort(arr):
    """
    Implement the gravity sort (Bead sort) algorithm.
    
    Gravity sort works by simulating gravity dropping beads in an abacus-like manner.
    It sorts positive integers by stacking them vertically and letting gravity pull them down.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers or non-integer values.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for negative numbers or non-integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("Input must be a list of non-negative integers")
    
    # Find the maximum number to determine the number of "rows"
    max_num = max(arr)
    
    # Create a 2D representation of the numbers
    beads = [[1 if x > i else 0 for x in arr] for i in range(max_num)]
    
    # Let gravity pull the beads down
    sorted_arr = []
    for col in range(len(arr)):
        # Count the number of beads in each column
        col_count = max_num - sum(row[col] for row in beads)
        sorted_arr.append(col_count)
    
    return sorted(sorted_arr)