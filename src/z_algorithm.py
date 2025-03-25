def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm finds all occurrences of a pattern within a text in O(n+m) time complexity,
    where n is the length of the text and m is the length of the pattern.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of indices where the pattern starts in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Construct the Z array
    def compute_z_array(s):
        n = len(s)
        z = [0] * n
        left, right = 0, 0
        
        for k in range(1, n):
            # If k is outside the current Z-box, compute Z[k] normally
            if k > right:
                left = right = k
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                # k is inside the Z-box
                k1 = k - left
                
                # If the value does not stretch to the right edge of Z-box, 
                # just copy the value
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    # Otherwise, need to do more comparisons
                    left = k
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        
        return z
    
    # Combine pattern and text for Z algorithm
    search_string = pattern + '$' + text
    z_array = compute_z_array(search_string)
    
    # Find matches
    matches = []
    pattern_length = len(pattern)
    for i in range(pattern_length + 1, len(z_array)):
        if z_array[i] == pattern_length:
            matches.append(i - pattern_length - 1)
    
    return matches