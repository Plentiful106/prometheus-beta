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
    def replace_single_vowel(vowel):
        """Replace a single vowel with precisely defined mapping."""
        vowel_map = {
            'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o',
            'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'
        }
        return vowel_map.get(vowel, vowel)

    # Replace vowels while preserving other characters
    return ''.join(replace_single_vowel(char) for char in input_string)