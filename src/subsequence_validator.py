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

    # If string is less than 4 letters long, it's not valid
    if len(s) < 4:
        return False

    # Define vowels
    vowels = set('aeiou')

    # Recursive function to validate divisions
    def validate_division(current_s):
        # If current string is too short, return False
        if len(current_s) < 2:
            return False
        
        # First, check if current can be divided into valid subsequences
        is_vowel_possible = all(char in vowels for char in current_s)
        is_consonant_possible = all(char not in vowels for char in current_s)
        
        # Must be entirely uniform and at least 2 letters long 
        if (is_vowel_possible or is_consonant_possible) and len(current_s) >= 4:
            return True
        
        # Recursive exploration of divisions
        for i in range(2, len(current_s)):
            first_part = current_s[:i]
            rest = current_s[i:]
            
            # First part must be uniform
            first_is_vowels = all(char in vowels for char in first_part)
            first_is_consonants = all(char not in vowels for char in first_part)
            
            if (first_is_vowels or first_is_consonants) and len(first_part) >= 2:
                # Check rest of the string
                if len(rest) == 0:
                    return True
                
                # Recursively validate the rest
                if validate_division(rest):
                    return True
        
        return False

    return validate_division(s)