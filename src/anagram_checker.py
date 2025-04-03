import unicodedata

def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.

    An anagram is a word formed by rearranging the letters of another word,
    using all the original letters exactly once.

    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare

    Returns:
        bool: True if the words are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
        ValueError: If either input is an empty string
    """
    # Validate input types
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Both inputs must be strings")
    
    # Validate input is not empty
    if not word1 or not word2:
        raise ValueError("Inputs cannot be empty strings")
    
    # Normalize inputs by converting to lowercase, removing whitespace, 
    # and stripping diacritical marks
    def normalize(s: str) -> str:
        # Normalize to decomposed form, remove diacritical marks, then remove non-ascii letters
        return ''.join(
            char for char in unicodedata.normalize('NFKD', s.lower().replace(" ", ""))
            if not unicodedata.combining(char)
        )
    
    normalized_word1 = normalize(word1)
    normalized_word2 = normalize(word2)
    
    # Check if lengths match
    if len(normalized_word1) != len(normalized_word2):
        return False
    
    # Compare character counts
    return sorted(normalized_word1) == sorted(normalized_word2)