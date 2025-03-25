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
                
                # Validate rest of string with same type
                def is_rest_valid_type(rest_str):
                    for check_len in range(2, len(rest_str) + 1):
                        for i in range(len(rest_str) - check_len + 1):
                            subseq = rest_str[i:i+check_len]
                            if not (
                                (is_initial_vowel and all(char in vowels for char in subseq)) or
                                (is_initial_consonant and all(char not in vowels for char in subseq))
                            ):
                                return False
                    return True
                
                # Check if rest can be divided into same type subsequences
                if is_rest_valid_type(rest):
                    return True
        
        return False

    return validate_division(s)