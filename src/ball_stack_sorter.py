from typing import List, Literal, Dict
from copy import deepcopy

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
        # Define the order for sorting
        order = ['Red', 'Blue', 'Green']
        
        # Maximum allowed moves
        max_moves = self.original_size * 9
        
        # Try different sorting strategies
        moves = 0
        while moves < max_moves:
            # Check if sorted
            if all(len(set(stack)) == 1 for stack in self.stacks.values()):
                return True
            
            # Comprehensive ball redistribution
            for color in order:
                # Identify which stacks have non-color balls
                non_color_indices = [
                    i for i, ball in enumerate(self.stacks[color]) 
                    if ball != color
                ]
                
                # Move non-matching balls out
                if non_color_indices:
                    non_match_ball_index = non_color_indices[0]
                    non_match_ball = self.stacks[color].pop(non_match_ball_index)
                    
                    # Try moving to another stack
                    other_stacks = [c for c in order if c != color]
                    moved = False
                    for dest in other_stacks:
                        # Only move if destination is not full
                        self.stacks[dest].append(non_match_ball)
                        moves += 1
                        moved = True
                        break
                    
                    if not moved:
                        # Reset if unable to move
                        self.stacks[color].insert(non_match_ball_index, non_match_ball)
            
            # Prevent excessive iterations
            if moves >= max_moves:
                return False
        
        return False