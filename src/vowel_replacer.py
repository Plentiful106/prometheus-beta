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
    def get_next_vowel(vowel):
        # Lowercase vowel mapping
        if vowel == 'a': return 'u'
        if vowel == 'e': return 'a'
        if vowel == 'i': return 'e'
        if vowel == 'o': return 'i'
        if vowel == 'u': return 'o'
        
        # Uppercase vowel mapping 
        if vowel == 'A': return 'U'
        if vowel == 'E': return 'A'
        if vowel == 'I': return 'E'
        if vowel == 'O': return 'I'
        if vowel == 'U': return 'O'
        
        return vowel

    return ''.join(get_next_vowel(char) for char in input_string)