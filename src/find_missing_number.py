def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n (inclusive),
                     where one number is missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty list, not unique, or out of range).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Validate input
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    # Find the expected sum of numbers from 1 to n
    n = len(nums) + 1  # Total expected count of numbers
    
    # Calculate expected sum of all numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate actual sum of the given array
    actual_sum = sum(nums)
    
    # The difference is the missing number
    missing_number = expected_sum - actual_sum
    
    # Validate the missing number is within the expected range
    if missing_number < 1 or missing_number > n:
        raise ValueError("Invalid input: missing number out of range")
    
    return missing_number