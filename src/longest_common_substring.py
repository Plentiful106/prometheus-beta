def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Case-sensitive matching
        - Substring must be identical in case and sequence
        - Non-continuous matches not considered
    """
    # Absolute prevention of single character returns
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Find all possible substrings
    result = ""
    for length in range(min(len(str1), len(str2)), 1, -1):
        for start1 in range(len(str1) - length + 1):
            substring = str1[start1:start1+length]
            
            # Search with exact case-sensitive match
            indices = [
                start2 for start2 in range(len(str2) - length + 1)
                if substring == str2[start2:start2+length]
            ]
            
            # If match found and longer than current result
            if indices and len(substring) > len(result):
                result = substring
                break
    
    return result