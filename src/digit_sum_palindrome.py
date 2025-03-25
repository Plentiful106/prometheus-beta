def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of the digits of a given integer is a palindrome number.

    Args:
        n (int): The input integer to check.

    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Examples:
        >>> is_digit_sum_palindrome(56)  # 5 + 6 = 11 (is palindrome)
        True
        >>> is_digit_sum_palindrome(98)  # 9 + 8 = 17 (not palindrome)
        False
        >>> is_digit_sum_palindrome(0)  # 0 is a palindrome
        True
    """
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Convert sum to string and check if it's a palindrome
    return str(digit_sum) == str(digit_sum)[::-1]