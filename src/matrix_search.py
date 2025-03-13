def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If matrix is empty or contains non-integer elements
    
    Time Complexity: O(m * n), where m is number of rows and n is number of columns
    Space Complexity: O(1)
    """
    # Validate input type
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list of lists")
    
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return False
    
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    # Check if all elements are numeric
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("Matrix must contain only numeric values")
    
    # Perform matrix search
    for row in matrix:
        if target in row:
            return True
    
    return False