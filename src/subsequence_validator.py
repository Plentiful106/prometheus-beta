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
    def validate_division(current_s, min_length=2):
        # If current string is too short, return False
        if len(current_s) < min_length:
            return False
        
        # First, determine the type of subsequence (vowels or consonants)
        is_vowel_seq = all(char in vowels for char in current_s[:min_length])
        is_consonant_seq = all(char not in vowels for char in current_s[:min_length])
        
        # If first subsequence doesn't meet minimum length or isn't uniform, return False
        if not (is_vowel_seq or is_consonant_seq):
            return False
        
        # If this is the entire string and it meets requirements, return True
        if len(current_s) == min_length:
            return True
        
        # Check rest of the string recursively
        rest = current_s[min_length:]
        
        # Must maintain same type of subsequence
        if is_vowel_seq:
            return all(char in vowels for char in rest[:min_length]) and \
                   validate_division(rest, min_length)
        else:  # consonant sequence
            return all(char not in vowels for char in rest[:min_length]) and \
                   validate_division(rest, min_length)

    # Try validation starting at length 2
    return validate_division(s)