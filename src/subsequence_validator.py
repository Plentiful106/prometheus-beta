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
    def validate_division(start_index):
        # If we've processed the entire string, check if start is at the end
        if start_index == len(chars):
            return True
        
        # Try subsequences of 2 to remaining length
        for length in range(2, len(chars) - start_index + 1):
            subseq = chars[start_index:start_index+length]
            
            # Check if subsequence is valid (all vowels or all consonants)
            is_all_vowels = all(char in vowels for char in subseq)
            is_all_consonants = all(char not in vowels for char in subseq)
            
            # If valid subsequence found, recursively validate rest of string
            if (is_all_vowels or is_all_consonants) and length >= 2:
                if validate_division(start_index + length):
                    return True
        
        return False

    return validate_division(0)