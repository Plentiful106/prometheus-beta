def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Check input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Remove whitespace and convert to lowercase for consistent comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count characters in first string
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    # Count characters in second string
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2