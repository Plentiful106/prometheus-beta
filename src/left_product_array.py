def left_product_array(nums):
    """
    Calculate an array where each element is the product of all numbers to the left 
    of the corresponding element in the original array.

    Args:
        nums (list): Input list of numbers.

    Returns:
        list: Array where each element is the product of numbers to its left.

    Raises:
        TypeError: If input is not a list.
        ValueError: If input contains non-numeric elements.

    Examples:
        >>> left_product_array([1, 2, 3, 4])
        [1, 1, 2, 6]
        >>> left_product_array([])
        []
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not nums:
        return []
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numeric")
    
    # Initialize the result array and left product
    result = [1] * len(nums)
    left_product = 1
    
    # Calculate left products
    for i in range(len(nums)):
        result[i] = left_product
        left_product *= nums[i]
    
    return result