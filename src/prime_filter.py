def is_prime(n):
    """
    Check if a given number is prime.
    
    A prime number is a number greater than 1 that has no divisors 
    other than 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check for valid input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def filter_primes(numbers):
    """
    Filter a list of integers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the prime numbers from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check for valid input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are integers
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]