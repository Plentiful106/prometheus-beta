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
    def replace_single_vowel(char):
        # Lowercase replacements
        if char == 'a': return 'u'
        if char == 'e': return 'a'
        if char == 'i': return 'e'
        if char == 'o': return 'i'
        if char == 'u': return 'o'
        
        # Uppercase replacements
        if char == 'A': return 'U'
        if char == 'E': return 'A'
        if char == 'I': return 'E'
        if char == 'O': return 'I'
        if char == 'U': return 'O'
        
        return char

    # Replace vowels while preserving other characters
    return ''.join(replace_single_vowel(char) for char in input_string)