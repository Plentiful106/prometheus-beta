from typing import List, Literal

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
    
    def _move_ball(self, from_stack: str, to_stack: str):
        """
        Move a single ball from one stack to another.
        
        Args:
            from_stack (str): Source stack color
            to_stack (str): Destination stack color
        
        Raises:
            ValueError: If the source stack is empty
        """
        if not self.stacks[from_stack]:
            raise ValueError(f"Cannot move ball from empty {from_stack} stack")
        
        ball = self.stacks[from_stack].pop()
        self.stacks[to_stack].append(ball)
    
    def sort(self) -> bool:
        """
        Sort the stacks such that each stack contains only one color.
        
        Returns:
            bool: True if sorting is successful, False otherwise
        """
        # Total number of moves is bounded by the number of balls
        max_moves = self.original_size * 6  # Increased to allow more movement
        moves = 0
        
        while moves < max_moves:
            # Check if all stacks are sorted (each contains only one color)
            if all(len(set(stack)) == 1 for stack in self.stacks.values()):
                return True
            
            # Comprehensive color movement strategy
            for source in ['Red', 'Blue', 'Green']:
                for dest in ['Red', 'Blue', 'Green']:
                    if source != dest and len(set(self.stacks[source])) > 1:
                        # Move ball if current source stack is not pure
                        self._move_ball(source, dest)
                        moves += 1
                        break
                    
                if moves >= max_moves:
                    break
        
        return False