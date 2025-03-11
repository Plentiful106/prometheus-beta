def quickselect(arr, k):
    """
    Implement the quickselect algorithm to find the kth smallest element in an array.
    
    Args:
        arr (list): A list of comparable elements to search through
        k (int): The k-th smallest element to find (1-based indexing)
    
    Returns:
        The k-th smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or the input is invalid
    """
    # Validate input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Adjust k to 0-based indexing
    k -= 1
    
    def partition(left, right):
        """
        Partition the array and return the pivot index.
        
        Args:
            left (int): Left boundary of the subarray
            right (int): Right boundary of the subarray
        
        Returns:
            int: The final position of the pivot element
        """
        # Choose the rightmost element as pivot
        pivot = arr[right]
        
        # Pointer for greater element
        i = left - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(left, right):
            if arr[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    def quickselect_recursive(left, right):
        """
        Recursive helper function to find k-th smallest element.
        
        Args:
            left (int): Left boundary of the subarray
            right (int): Right boundary of the subarray
        
        Returns:
            The k-th smallest element
        """
        # If the array contains a single element, return that element
        if left == right:
            return arr[left]
        
        # Partition the array
        pivot_index = partition(left, right)
        
        # If the position is the same as k, return the element
        if k == pivot_index:
            return arr[k]
        
        # If k is less than the pivot index, search in the left subarray
        if k < pivot_index:
            return quickselect_recursive(left, pivot_index - 1)
        
        # If k is greater than the pivot index, search in the right subarray
        return quickselect_recursive(pivot_index + 1, right)
    
    # Call the recursive helper with full array bounds
    return quickselect_recursive(0, len(arr) - 1)