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
        - Substring must match exactly in case and sequence
    """
    # Precisely define substring matching rules
    result = ""
    for length in range(min(len(str1), len(str2)), 1, -1):
        for start1 in range(len(str1) - length + 1):
            substring = str1[start1:start1+length]
            
            # Scan for exact match in str2, character by character
            for start2 in range(len(str2) - length + 1):
                match = True
                for k in range(length):
                    if substring[k] != str2[start2+k]:
                        match = False
                        break
                
                # If perfectly matched, update result
                if match:
                    result = substring
                    return result
    
    return result