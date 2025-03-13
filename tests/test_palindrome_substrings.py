import pytest
from src.palindrome_substrings import find_shortest_palindrome_substrings

def test_find_shortest_palindrome_substrings_basic():
    assert find_shortest_palindrome_substrings("aabaa") == ['a', 'aa']
    assert find_shortest_palindrome_substrings("abba") == ['a', 'b', 'bb', 'abba']
    assert find_shortest_palindrome_substrings("racecar") == ['r', 'a', 'c', 'e', 'racecar']

def test_find_shortest_palindrome_substrings_edge_cases():
    # Empty string
    assert find_shortest_palindrome_substrings("") == []
    
    # Single character
    assert find_shortest_palindrome_substrings("a") == ['a']
    
    # No palindromes except single characters
    assert find_shortest_palindrome_substrings("abc") == ['a', 'b', 'c']

def test_find_shortest_palindrome_substrings_complex():
    # More complex cases
    assert find_shortest_palindrome_substrings("bananas") == ['a', 'n']
    assert find_shortest_palindrome_substrings("hello") == ['l', 'h', 'e', 'o']

def test_find_shortest_palindrome_substrings_duplicates():
    # Ensure duplicates are handled correctly
    assert find_shortest_palindrome_substrings("aaaa") == ['a', 'aa']

def test_find_shortest_palindrome_substrings_mixed_case():
    # Mixed case sensitivity
    assert find_shortest_palindrome_substrings("AbBa") == ['A', 'b', 'B', 'a']