def solve_knapsack(items, capacity):
    """
    Solve the Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid (negative weights/values or non-integer capacity)
    """
    # Input validation
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("Capacity must be a non-negative integer")
    
    if not items:
        return 0
    
    # Validate items
    for weight, value in items:
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Item weights must be non-negative numbers")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item values must be non-negative numbers")
    
    # Dynamic Programming solution
    n = len(items)
    # Create a 2D table to store maximum values
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Current item's weight and value
            current_weight, current_value = items[i-1]
            
            # If including the current item exceeds capacity, skip it
            if current_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude current item
                    dp[i-1][w - current_weight] + current_value  # include current item
                )
    
    # Return maximum value
    return dp[n][capacity]