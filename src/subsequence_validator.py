def can_divide_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into 
    subsequences of at least 2 letters where each subsequence is either 
    all vowels or all consonants.

    Args:
        s (str): A string of lowercase English letters

    Returns:
        bool: True if the string can be divided into valid subsequences, 
              False otherwise

    Raises:
        ValueError: If the input contains characters other than lowercase letters
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels
    vowels = set('aeiou')

    # Helper function to check if a sequence is all vowels or all consonants
    def is_valid_subsequence(subseq):
        return len(subseq) >= 2 and (
            all(char in vowels for char in subseq) or 
            all(char not in vowels for char in subseq)
        )

    # Try all possible divisions
    def can_divide(current_string):
        # Base cases
        if len(current_string) < 2:
            return False
        
        # If the entire string is a valid subsequence, return True
        if is_valid_subsequence(current_string):
            return True
        
        # Try all possible divisions
        for i in range(2, len(current_string) + 1):
            # Check if first subsequence is valid
            if is_valid_subsequence(current_string[:i]):
                # Recursively check the rest of the string
                if i == len(current_string) or can_divide(current_string[i:]):
                    return True
        
        return False

    return can_divide(s)