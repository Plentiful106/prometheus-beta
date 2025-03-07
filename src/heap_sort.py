def heap_sort(arr):
    """
    Implement the Heap Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains elements that cannot be compared.
    """
    # Create a copy of the input list to avoid modifying the original
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def heapify(arr, n, i):
        """
        Heapify a subtree rooted with node i.
        
        Args:
            arr (list): The list to heapify
            n (int): Size of the heap
            i (int): Root index of the subtree
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # Check if right child exists and is larger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    # Build max heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)
    
    return arr