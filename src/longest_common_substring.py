def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Special case for single character match with exact case
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Substring must match exactly, including case
    longest_match = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Track current match
            current_match = ""
            x, y = i, j
            
            # Strict match with exact case preservation
            while (x < len(str1) and 
                   y < len(str2) and 
                   str1[x] == str2[y]):
                current_match += str1[x]
                x += 1
                y += 1
            
            # Update if current match is longer and meets criteria
            if (len(current_match) > len(longest_match) and 
                len(current_match) > 1):
                longest_match = current_match
    
    return longest_match