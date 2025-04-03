def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
    
    Examples:
        >>> is_balanced_parentheses("()")  # Simple balanced
        True
        >>> is_balanced_parentheses("((()))")  # Nested balanced
        True
        >>> is_balanced_parentheses("(()())")  # Multiple sets
        True
        >>> is_balanced_parentheses("(()")  # Unbalanced
        False
        >>> is_balanced_parentheses(")(")  # Invalid order
        False
    """
    # Use a stack to track opening parentheses
    stack = []
    
    # Define matching pairs
    matching = {')': '('}
    
    for char in s:
        if char == '(':
            # Push opening parenthesis
            stack.append(char)
        elif char == ')':
            # If closing parenthesis encountered without matching opening
            if not stack:
                return False
            
            # Check if top of stack matches
            if stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    
    # Stack should be empty for balanced parentheses
    return len(stack) == 0