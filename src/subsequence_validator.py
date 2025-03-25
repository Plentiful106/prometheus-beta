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
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels
    vowels = set('aeiou')

    # Convert to list for easier manipulation
    chars = list(s)
    
    # Try to divide into valid subsequences
    def validate_division(start_index, prev_type=None):
        # If we've processed the entire string, return True if valid
        if start_index == len(chars):
            return True
        
        # Try subsequences of 2 to remaining length
        for length in range(2, len(chars) - start_index + 1):
            subseq = chars[start_index:start_index+length]
            
            # Check if this would be the last possible division
            is_last_possible_division = start_index + length == len(chars)
            
            # Determine if current subsequence is vowels or consonants
            is_all_vowels = all(char in vowels for char in subseq)
            is_all_consonants = all(char not in vowels for char in subseq)
            
            # Validate subsequence
            if is_all_vowels or is_all_consonants:
                # First subsequence
                if prev_type is None:
                    current_type = 'vowels' if is_all_vowels else 'consonants'
                    # For the first subsequence, continue dividing
                    if validate_division(start_index + length, current_type):
                        return True
                # Subsequent subsequences: must match previous type AND use entire string
                elif (prev_type == 'vowels' and is_all_vowels) or \
                     (prev_type == 'consonants' and is_all_consonants):
                    # If this is the last possible division, ensure full string is used
                    if is_last_possible_division or \
                       validate_division(start_index + length, prev_type):
                        return True
        
        return False

    return validate_division(0)