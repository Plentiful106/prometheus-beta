from typing import List, TypeVar, Union
import heapq

T = TypeVar('T')

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is a sorting algorithm based on the card game patience (solitaire).
    It works by creating piles and then merging them using a min-heap.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create piles (like in patience game)
    piles = []
    
    for item in arr:
        # Find the correct pile to place the item
        # If no suitable pile, create a new pile
        found_pile = False
        for pile in piles:
            if not pile or item <= pile[-1]:
                pile.append(item)
                found_pile = True
                break
        
        # If no existing pile works, create a new pile
        if not found_pile:
            piles.append([item])
    
    # Merge piles using a min heap
    result = []
    heap = [(pile[-1], i) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    while heap:
        val, pile_index = heapq.heappop(heap)
        result.append(val)
        
        # Remove the top element from the corresponding pile
        piles[pile_index].pop()
        
        # If pile is not empty, add its top element to heap
        if piles[pile_index]:
            heapq.heappush(heap, (piles[pile_index][-1], pile_index))
    
    return result