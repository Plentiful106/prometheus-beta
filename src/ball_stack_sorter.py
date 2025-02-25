from typing import List, Literal
from collections import Counter

Color = Literal['Red', 'Blue', 'Green']

class BallStackSorter:
    def __init__(self, red_stack: List[Color], blue_stack: List[Color], green_stack: List[Color]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        Args:
            red_stack (List[Color]): Stack of balls (include red balls)
            blue_stack (List[Color]): Stack of balls (include blue balls)
            green_stack (List[Color]): Stack of balls (include green balls)
        """
        self._validate_input(red_stack, blue_stack, green_stack)
        self.stacks = {
            'Red': red_stack.copy(),
            'Blue': blue_stack.copy(),
            'Green': green_stack.copy()
        }
        self.original_size = len(red_stack)
        
    @staticmethod
    def _validate_input(red_stack: List[Color], blue_stack: List[Color], green_stack: List[Color]):
        """
        Validate initial stack conditions.
        
        Args:
            red_stack (List[Color]): Stack of red balls
            blue_stack (List[Color]): Stack of blue balls
            green_stack (List[Color]): Stack of green balls
        
        Raises:
            ValueError: If stacks have unequal lengths
        """
        # Check if all stacks have the same length
        stack_lengths = [len(red_stack), len(blue_stack), len(green_stack)]
        if len(set(stack_lengths)) > 1:
            raise ValueError("All stacks must have equal number of balls")
        
        # Check if all items are strings and match the color domain
        valid_colors = {'Red', 'Blue', 'Green'}
        for stack_name, stack in [('Red', red_stack), ('Blue', blue_stack), ('Green', green_stack)]:
            if not all(isinstance(ball, str) and ball in valid_colors for ball in stack):
                raise ValueError(f"Invalid color in {stack_name} stack")
    
    def sort(self) -> bool:
        """
        Sort the stacks such that each stack contains only one color.
        
        Returns:
            bool: True if sorting is successful, False otherwise
        """
        # Maximum allowed moves
        max_moves = self.original_size * 12
        moves = 0
        
        # Pre-compute the preferred color for each stack
        color_order = {
            'Red': 'Red',
            'Blue': 'Blue', 
            'Green': 'Green'
        }
        
        while moves < max_moves:
            # Check if sorted
            if all(len(set(stack)) == 1 for stack in self.stacks.values()):
                return True
            
            # Most complex sorting strategy
            for color, stack in self.stacks.items():
                # Target color for this stack
                target_color = color_order[color]
                
                # Color count in current stack
                color_count = Counter(stack)
                
                # If stack is not pure
                if len(set(stack)) > 1:
                    # Find a ball that doesn't match the stack's color
                    for i, ball in enumerate(stack):
                        if ball != target_color:
                            # Remove this ball
                            non_target = stack.pop(i)
                            moves += 1
                            
                            # Attempt to redistribute
                            redistributed = False
                            for other_color in ['Red', 'Blue', 'Green']:
                                if other_color != color and len(self.stacks[other_color]) < self.original_size:
                                    self.stacks[other_color].append(non_target)
                                    redistributed = True
                                    break
                            
                            # If redistribution fails, put back
                            if not redistributed:
                                stack.insert(i, non_target)
                            
                            break
            
            # If moves are exhausted, exit
            if moves >= max_moves:
                return False
        
        return False