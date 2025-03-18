from typing import List, TypeVar, Comparable

T = TypeVar('T', bound=Comparable)

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience Sort is a sorting algorithm based on the card game patience (solitaire).
    It works by creating piles (like in patience) and then merging them.
    
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
            if not pile or item >= pile[-1]:
                pile.append(item)
                found_pile = True
                break
        
        # If no existing pile works, create a new pile
        if not found_pile:
            piles.append([item])
    
    # Merge piles
    result = []
    while piles:
        # Find the pile with the smallest top card
        smallest_pile_index = min(range(len(piles)), key=lambda i: piles[i][-1])
        
        # Add the top card of the smallest pile to result
        result.append(piles[smallest_pile_index].pop())
        
        # Remove pile if it becomes empty
        if not piles[smallest_pile_index]:
            piles.pop(smallest_pile_index)
    
    return result