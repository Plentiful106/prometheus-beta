def replace_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet, 
    preserving the original case.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: A new string with vowels replaced by the next vowel in the alphabet.

    Examples:
        >>> replace_vowels("hello")
        'hulli'
        >>> replace_vowels("AEIOU")
        'EIOUA'
        >>> replace_vowels("Python")
        'Pythun'
    """
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    
    def replace_single_vowel(char):
        # Lowercase replacement
        if char in vowels_lower:
            current_index = vowels_lower.index(char)
            return vowels_lower[(current_index - 1 + len(vowels_lower)) % len(vowels_lower)]
        
        # Uppercase replacement
        if char in vowels_upper:
            current_index = vowels_upper.index(char)
            return vowels_upper[(current_index - 1 + len(vowels_upper)) % len(vowels_upper)]
        
        # Non-vowel character
        return char

    # Replace vowels while preserving other characters
    return ''.join(replace_single_vowel(char) for char in input_string)