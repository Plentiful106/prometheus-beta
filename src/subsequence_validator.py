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
        return all(char in vowels for char in subseq) or \
               all(char not in vowels for char in subseq)

    # Try all possible divisions
    for length in range(2, len(s) + 1):
        # Check if we can divide the entire string into valid subsequences of the current length
        for start in range(len(s) - length + 1):
            # Generate all possible subsequences of current length
            valid_division = True
            for i in range(start, len(s), length):
                # Check if we have a complete subsequence of the current length
                if i + length > len(s):
                    break
                
                subseq = s[i:i+length]
                if not is_valid_subsequence(subseq):
                    valid_division = False
                    break
            
            # If we found a valid division of the entire string, return True
            if valid_division and start + (len(s) // length) * length == len(s):
                return True

    return False