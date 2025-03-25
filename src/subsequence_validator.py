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

    # Helper function to check if a sequence is all vowels or all consonants
    def is_valid_subsequence(subseq):
        return len(subseq) >= 2 and (
            all(char in vowels for char in subseq) or 
            all(char not in vowels for char in subseq)
        )

    # Recursive function to check divisions
    def check_division(current_s):
        # If less than 2 letters, can't divide
        if len(current_s) < 2:
            return False
        
        # Try all possible first subsequence lengths
        for first_len in range(2, len(current_s) + 1):
            first_subseq = current_s[:first_len]
            
            # If first subsequence is valid
            if is_valid_subsequence(first_subseq):
                # If no more letters, we succeeded
                if first_len == len(current_s):
                    return True
                
                # Recursively check rest of the string
                if check_division(current_s[first_len:]):
                    return True
        
        return False

    return check_division(s)