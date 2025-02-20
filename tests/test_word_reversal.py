import pytest
from src.word_reversal import reverse_words

def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_reverse_words_single_word():
    assert reverse_words("Hello") == "Hello"

def test_reverse_words_empty_string():
    assert reverse_words("") == ""

def test_reverse_words_multiple_spaces():
    assert reverse_words("   Hello    World   ") == "World Hello"

def test_reverse_words_with_punctuation():
    assert reverse_words("Hello, World!") == "World! Hello,"

def test_reverse_words_different_lengths():
    assert reverse_words("a very long sentence") == "sentence long very a"