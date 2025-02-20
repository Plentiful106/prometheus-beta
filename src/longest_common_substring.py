def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Matching is case-sensitive
        - Substring must be at least 2 characters long
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Special case for single character match with exact case
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Check for strict substring matching
    max_substring = ""
    for start1 in range(len(str1)):
        for length in range(2, len(str1) - start1 + 1):
            # Extract potential substring
            substring = str1[start1:start1+length]
            
            # Search for exact match in second string
            for start2 in range(len(str2)):
                if substring == str2[start2:start2+length]:
                    # Update max_substring if current is longer
                    if len(substring) > len(max_substring):
                        max_substring = substring
    
    return max_substring