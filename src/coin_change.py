def min_coins(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): Available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed, or -1 if exact change is impossible
    
    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate input
    if not coins or not isinstance(coins, list):
        raise ValueError("Coins must be a non-empty list")
    
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("Amount must be a non-negative integer")
    
    # Remove invalid coins and sort in descending order
    valid_coins = sorted([coin for coin in coins if isinstance(coin, int) and coin > 0], reverse=True)
    
    if not valid_coins:
        raise ValueError("No valid coin denominations provided")
    
    # Dynamic programming solution
    # Initialize with max possible value
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Compute minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in valid_coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if change is impossible
    return dp[amount] if dp[amount] != float('inf') else -1