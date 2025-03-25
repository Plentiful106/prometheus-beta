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

    # Recursive function to validate divisions
    def validate_division(s):
        # If string is too short, return False
        if len(s) < 2:
            return False
        
        # Find all valid divisions
        for divide_length in range(2, len(s) + 1):
            # Initial subsequence must be valid
            initial_part = s[:divide_length]
            is_initial_vowel = all(char in vowels for char in initial_part)
            is_initial_consonant = all(char not in vowels for char in initial_part)
            
            # If initial part is valid
            if is_initial_vowel or is_initial_consonant:
                # If this is the entire string, return True
                if divide_length == len(s):
                    return True
                
                # Recursively check the rest of the string
                rest = s[divide_length:]
                is_rest_valid = validate_division(rest)
                
                # Must be same type of subsequence
                if is_rest_valid and (
                    (is_initial_vowel and all(char in vowels for char in rest[:len(rest) for length in range(2, len(rest)+1)]) or
                    (is_initial_consonant and all(char not in vowels for char in rest[:len(rest) for length in range(2, len(rest)+1)])
                )):
                    return True
        
        return False

    return validate_division(s)