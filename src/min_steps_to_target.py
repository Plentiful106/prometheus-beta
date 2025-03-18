from typing import List, Optional

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
    
    # Use dynamic programming to find minimum steps
    # We'll use a set to track all possible sums at each step
    current_sums = {0}
    steps = 0
    
    # We'll sort the numbers to optimize processing
    sorted_nums = sorted(numbers)
    
    while current_sums:
        # If target is in current sums, we've found the minimum steps
        if target in current_sums:
            return steps
        
        # If we've used all numbers and can't reach target, return None
        if steps >= len(numbers):
            return None
        
        # Generate new possible sums by adding or subtracting the next number
        next_num = sorted_nums[steps]
        new_sums = set()
        
        for current_sum in current_sums:
            # Try adding the number
            new_sums.add(current_sum + next_num)
            # Try subtracting the number
            new_sums.add(current_sum - next_num)
        
        # Update current sums and increment steps
        current_sums = new_sums
        steps += 1
    
    # If no solution found
    return None