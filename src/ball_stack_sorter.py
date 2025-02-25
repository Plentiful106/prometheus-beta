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
        max_moves = self.original_size * 15  # Significantly increased move limit
        moves = 0
        
        # Order defines the target distribution
        order = ['Red', 'Blue', 'Green']
        
        while moves < max_moves:
            # Quick check for sorted stacks
            if all(len(set(stack)) == 1 for stack in self.stacks.values()):
                return True
            
            # Comprehensive sorting approach
            for current_color in order:
                # If current stack is not pure
                if len(set(self.stacks[current_color])) > 1:
                    # Try to move a non-matching ball
                    for i, ball in enumerate(self.stacks[current_color]):
                        if ball != current_color:
                            # Remove ball from current stack
                            non_matching_ball = self.stacks[current_color].pop(i)
                            moves += 1
                            
                            # Find the best destination
                            destination_found = False
                            for dest_color in order:
                                # Destination must not be the current stack and must have space
                                if dest_color != current_color and len(self.stacks[dest_color]) < self.original_size:
                                    self.stacks[dest_color].append(non_matching_ball)
                                    destination_found = True
                                    break
                            
                            # If no destination was found, put back
                            if not destination_found:
                                self.stacks[current_color].insert(i, non_matching_ball)
                                moves -= 1
                            
                            break
            
            # Prevent infinite loop
            if moves >= max_moves:
                return False
        
        return False