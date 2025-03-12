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
    
    # If only one element, return it as-is
    if len(arr) == 1:
        return arr
    
    # Find the maximum number to create the abacus rows
    max_num = max(arr)
    
    # Create an "abacus" representation
    abacus = [[0] * len(arr) for _ in range(max_num)]
    
    # Place initial beads
    for col, num in enumerate(arr):
        for row in range(num):
            abacus[row][col] = 1
    
    # Let gravity pull beads down
    result = []
    for col in range(len(arr)):
        # Count beads from the bottom (gravity)
        bead_count = sum(abacus[row][col] for row in range(max_num))
        result.append(bead_count)
    
    return result