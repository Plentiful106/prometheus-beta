def find_single_unique_element(arr):
    """
    Find the single non-duplicate element in a sorted array.
    
    This function uses a binary search approach to efficiently find 
    the unique element in a sorted array where every other element 
    appears exactly twice.
    
    Args:
        arr (list): A sorted array of integers where all elements 
                    except one appear twice.
    
    Returns:
        int: The unique element that appears only once.
    
    Raises:
        ValueError: If the input array is None, empty, or does not 
                    contain a single unique element.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Example:
        >>> find_single_unique_element([1, 1, 2, 2, 3, 4, 4])
        3
    """
    # Validate input
    if not arr or len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Handle edge cases at the start and end of the array
        if left == right:
            return arr[left]
        
        # Check if mid is the unique element
        mid = left + (right - left) // 2
        
        # Check if mid is even or odd index
        if mid % 2 == 1:
            mid -= 1
        
        # Compare pairs around mid
        if arr[mid] == arr[mid + 1]:
            # Unique element is on the right side
            left = mid + 2
        else:
            # Unique element is on the left side or at mid
            right = mid
    
    # This should not be reached if input is valid
    raise ValueError("No unique element found")