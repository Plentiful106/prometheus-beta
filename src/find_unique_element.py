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
    
    # Handle first and last element edge cases
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if mid is not part of a pair
        if mid % 2 == 1:
            mid -= 1
        
        # Check if this mid is the start of a pair
        if mid + 1 < len(arr) and arr[mid] == arr[mid+1]:
            # Unique is on the right side
            left = mid + 2
        else:
            # Unique is on this side or to the left
            right = mid
        
        # If only one element left, that's our unique element
        if left == right:
            return arr[left]
    
    # This should not be reached if input is valid
    raise ValueError("No unique element found")