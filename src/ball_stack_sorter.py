from typing import List, Literal

Color = Literal['Red', 'Blue', 'Green']

class BallStackSorter:
    def __init__(self, red_stack: List[Color], blue_stack: List[Color], green_stack: List[Color]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        Args:
            red_stack (List[Color]): Stack of red balls
            blue_stack (List[Color]): Stack of blue balls
            green_stack (List[Color]): Stack of green balls
        """
        self.stacks = {
            'Red': red_stack,
            'Blue': blue_stack,
            'Green': green_stack
        }
        
    def _validate_input(self):
        """
        Validate initial stack conditions.
        
        Raises:
            ValueError: If stacks have unequal lengths or contain invalid colors
        """
        # Check if all stacks have the same length
        stack_lengths = [len(stack) for stack in self.stacks.values()]
        if len(set(stack_lengths)) > 1:
            raise ValueError("All stacks must have equal number of balls")
        
        # Check if all items are valid colors
        for stack_name, stack in self.stacks.items():
            if not all(isinstance(ball, str) and ball in ['Red', 'Blue', 'Green'] for ball in stack):
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
        
        Raises:
            ValueError: If initial stack conditions are invalid
        """
        # Validate input first
        self._validate_input()
        
        # Total number of moves is bounded by the number of balls
        max_moves = len(self.stacks['Red']) * 3
        moves = 0
        
        while moves < max_moves:
            # Check if all stacks are sorted (each contains only one color)
            if all(len(set(stack)) == 1 for stack in self.stacks.values()):
                return True
            
            # Strategy: move balls to create color-pure stacks
            for color1 in ['Red', 'Blue', 'Green']:
                for color2 in ['Red', 'Blue', 'Green']:
                    if color1 != color2:
                        # If color1 stack is not pure, try to move ball to color2 stack
                        if len(set(self.stacks[color1])) > 1:
                            self._move_ball(color1, color2)
                            moves += 1
                            break
            
            # Prevent infinite loop
            if moves >= max_moves:
                return False
        
        return False