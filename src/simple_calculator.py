def simple_calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number in the calculation.
        num2 (float): The second number in the calculation.
        operator (str): The arithmetic operation to perform.
                        Supported operators: '+', '-', '*', '/'

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operator is provided.
        ZeroDivisionError: If attempting to divide by zero.
    """
    # Validate input operator
    valid_operators = {'+', '-', '*', '/'}
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator. Supported operators are: {', '.join(valid_operators)}")
    
    # Convert inputs to float to handle integer and float inputs
    num1 = float(num1)
    num2 = float(num2)
    
    # Perform the calculation based on the operator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2