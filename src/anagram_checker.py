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
    
    # Normalize inputs by converting to lowercase and removing whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    # Check if lengths match
    if len(word1) != len(word2):
        return False
    
    # Compare character counts
    return sorted(word1) == sorted(word2)