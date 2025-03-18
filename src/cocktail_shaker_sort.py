def cocktail_shaker_sort(arr):
    """
    Implement the cocktail shaker sort (bidirectional bubble sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both 
    directions. It works by first moving the largest unsorted element to the 
    end, then the smallest unsorted element to the beginning, reducing the 
    range of unsorted elements with each pass.
    
    Args:
        arr (list): The list to be sorted. Must be a mutable sequence of comparable elements.
    
    Returns:
        list: A new sorted list with the same elements as the input.
    
    Raises:
        TypeError: If the input is not a list or contains uncomparable elements.
    """
    # Validate input explicitly
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = list(arr)
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Attempt to do a comparison to ensure elements are comparable
    try:
        # Dummy comparison
        min(arr)
    except TypeError as e:
        raise TypeError("List contains elements that cannot be compared") from e
    
    # Flag to optimize the algorithm by stopping if no swaps occur
    swapped = True
    start = 0
    end = len(arr) - 1
    
    while swapped:
        # Reset swapped flag for this pass
        swapped = False
        
        # Forward pass (like bubble sort)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
        
        # Reduce end point as the largest element is now at the end
        end -= 1
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Increase start point as the smallest element is now at the beginning
        start += 1
    
    return arr