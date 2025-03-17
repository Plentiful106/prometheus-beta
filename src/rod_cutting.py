def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    The Rod Cutting problem involves finding the maximum revenue 
    obtainable by cutting a rod of length n into smaller pieces.
    
    Args:
        prices (list): A list of prices where prices[i] is the price 
                       of a rod of length i+1.
        n (int): The length of the rod to be cut.
    
    Returns:
        int: The maximum revenue obtainable by cutting the rod.
    
    Raises:
        ValueError: If prices list is empty or n is negative.
    """
    # Validate input
    if not prices:
        raise ValueError("Prices list cannot be empty")
    if n < 0:
        raise ValueError("Rod length cannot be negative")
    
    # Ensure we don't exceed available prices
    max_length = len(prices)
    
    # Initialize dynamic programming table
    # dp[i] will store the maximum revenue for a rod of length i
    dp = [0] * (n + 1)
    
    # Compute maximum revenue for each rod length
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, min(i + 1, max_length + 1)):
            # Try cutting rod of length j and solving remaining rod
            # Ensure we only use available prices
            max_val = max(max_val, prices[j-1] if j <= max_length else 0 + 
                          (dp[i-j] if i-j >= 0 else 0))
        dp[i] = max_val
    
    return dp[n]