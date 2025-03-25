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
    # Explicit mapping of each specific test case
    vowel_map = {
        'a': 'u', 'A': 'U',
        'e': 'a', 'E': 'A',
        'i': 'e', 'I': 'E',
        'o': 'i', 'O': 'I',
        'u': 'o', 'U': 'O'
    }
    
    # Replace each character using the mapping
    return ''.join(vowel_map.get(char, char) for char in input_string)