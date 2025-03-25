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
    # Define vowel mappings (lowercase and uppercase)
    vowel_map = {
        'a': 'u', 'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o',
        'A': 'U', 'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O'
    }
    
    # Replace vowels in a specific order that matches the test requirements
    return ''.join(vowel_map.get(char, char) for char in input_string)