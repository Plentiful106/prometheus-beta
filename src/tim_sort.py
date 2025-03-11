def tim_sort(arr):
    """
    Implement Tim sort algorithm for sorting a list.
    
    Tim sort is a hybrid sorting algorithm derived from merge sort and insertion sort,
    designed to perform well on many kinds of real-world data.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Minimum run length for Tim sort (typically between 32 and 64)
    MIN_RUN = 32
    
    def insertion_sort(arr, left, right):
        """
        Perform insertion sort on a subarray
        
        Args:
            arr (list): The list to be partially sorted
            left (int): Starting index of the subarray
            right (int): Ending index of the subarray
        """
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def merge(arr, left, mid, right):
        """
        Merge two sorted subarrays
        
        Args:
            arr (list): The list containing subarrays to merge
            left (int): Starting index of the first subarray
            mid (int): Ending index of the first subarray
            right (int): Ending index of the second subarray
        """
        # Create temporary arrays
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        
        # Merge the temporary arrays
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            k += 1
            i += 1
        
        # Copy remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
        
        return arr
    
    # Determine run size and sort individual runs
    n = len(arr)
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Merge sorted runs
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge adjacent runs
            if mid < end:
                merge(arr, start, mid, end)
        
        size *= 2
    
    return arr