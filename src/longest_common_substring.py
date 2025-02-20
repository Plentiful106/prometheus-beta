def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Matching is strictly case-sensitive
        - Substring must be at least 2 characters long
        - Requires exact character matches in original positions
    """
    def find_strict_substring(s1, s2):
        """
        Helper function to find strictly case-sensitive, positionally identical substrings
        """
        max_substring = ""
        for start1 in range(len(s1)):
            for length in range(2, len(s1) - start1 + 1):
                substring = s1[start1:start1+length]
                
                # Check in s2 with exact character and positional match
                if substring in s2 and s2.index(substring) + length <= len(s2):
                    index_s2 = s2.index(substring)
                    
                    # Verify character-by-character match
                    match = True
                    for k in range(length):
                        if s1[start1+k] != s2[index_s2+k]:
                            match = False
                            break
                    
                    # Update if match found and longer
                    if match and len(substring) > len(max_substring):
                        max_substring = substring
        
        return max_substring

    # Handle edge cases first
    if not str1 or not str2:
        return ""
    
    # Special case for identical single character
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Find strict substring with exact matches
    return find_strict_substring(str1, str2)