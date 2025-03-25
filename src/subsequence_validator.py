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

    # Check if entire string is uniform
    is_vowel_possible = all(char in vowels for char in s)
    is_consonant_possible = all(char not in vowels for char in s)
    
    # Must be entirely uniform and at least 4 letters long 
    return is_vowel_possible or is_consonant_possible