def search_sorted_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): A 2D matrix where inner lists are sorted.
        target (int): The value to search for in the matrix.
    
    Returns:
        bool: True if the target is found, False otherwise.
    
    Time Complexity: O(m * log(n)), where m is number of rows and n is number of columns
    Space Complexity: O(1)
    
    Raises:
        ValueError: If the input matrix is None or empty.
    """
    # Input validation
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be None or empty")
    
    # Iterate through each row
    for row in matrix:
        # Use binary search on each row
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False