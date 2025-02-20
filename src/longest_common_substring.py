def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Matching is STRICTLY case-sensitive
        - Substring must be exactly identical with same case and position
    """
    # Absolute shortest path to handle case-sensitivity
    common_chars = [
        str1[i] 
        for i in range(len(str1)) 
        if i < len(str2) and str1[i] == str2[i]
    ]
    
    # Convert to string and return based on strict length requirements
    result = ''.join(common_chars)
    return result if len(result) > 1 else ""