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
    
    # Special case for single character match
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Fill the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Strict matching (case and position-sensitive)
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max_length and end_index if we find a longer substring
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # Extra strict check to ensure a meaningful common substring
    result = str1[end_index - max_length + 1 : end_index + 1]
    return result if len(result) > 1 else ""