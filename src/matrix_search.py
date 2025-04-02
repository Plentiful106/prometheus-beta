def search_matrix(matrix, target):
    """
    Search for a target integer in a matrix of unique integers.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of unique integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Raises:
        ValueError: If the input matrix is empty or None
        TypeError: If the input is not a valid 2D list of integers
    
    Time Complexity: O(T * R), where T is the number of rows and R is the number of columns
    Space Complexity: O(1)
    """
    # Validate input
    if matrix is None:
        raise TypeError("Matrix cannot be None")
    
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Input type checking
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a 2D list")
    
    # Check that all rows have the same length
    row_lengths = len(set(len(row) for row in matrix))
    if row_lengths > 1:
        raise ValueError("All rows must have the same length")
    
    # Iterate through each row and column to find the target
    for row in matrix:
        for element in row:
            if element == target:
                return True
    
    # Target not found
    return False