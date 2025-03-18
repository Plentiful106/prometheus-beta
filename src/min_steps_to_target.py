from typing import List, Optional
from itertools import combinations, product

def min_steps_to_target_sum(numbers: List[int], target: int) -> Optional[int]:
    """
    Calculate the minimum number of steps to reach a target sum using given numbers.
    
    Each number can be used only once, and steps can involve addition or subtraction.
    
    Args:
        numbers (List[int]): List of integers to use for reaching the target
        target (int): The target sum to reach
    
    Returns:
        Optional[int]: Minimum number of steps to reach the target, or None if impossible
    
    Raises:
        ValueError: If input list is empty
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Special case: single number same as target
    if target in numbers:
        return 1
    
    # Remove duplicates but preserve order
    unique_nums = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    
    # Check all possible combinations
    for num_steps in range(2, len(unique_nums) + 1):
        for combo in combinations(unique_nums, num_steps):
            # Try all possible sign combinations
            for signs in product([1, -1], repeat=num_steps):
                # Compute sum with current sign combination
                current_sum = sum(num * sign for num, sign in zip(combo, signs))
                
                # If we reached the target, return number of steps
                if current_sum == target:
                    return num_steps
    
    # If no solution found
    return None