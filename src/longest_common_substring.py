def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - ABSOLUTE case sensitivity
        - EXACT character match with preservation of original case
    """
    # Ultra-strict case matching
    longest = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Start with current characters
            current = ""
            pos1, pos2 = i, j
            
            # Strict character-by-character matching
            while (pos1 < len(str1) and 
                   pos2 < len(str2) and 
                   str1[pos1] == str2[pos2]):
                current += str1[pos1]
                pos1 += 1
                pos2 += 1
            
            # Update longest only if strictly longer and meaningful
            if len(current) > len(longest) and len(current) > 1:
                longest = current
    
    return longest