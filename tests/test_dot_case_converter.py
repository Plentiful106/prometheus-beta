import pytest
from src.dot_case_converter import to_dot_case

def test_basic_camel_case():
    assert to_dot_case("helloWorld") == "hello.world"

def test_pascal_case():
    assert to_dot_case("HelloWorld") == "hello.world"

def test_snake_case():
    assert to_dot_case("hello_world") == "hello.world"

def test_kebab_case():
    assert to_dot_case("hello-world") == "hello.world"

def test_space_separated():
    assert to_dot_case("Hello World") == "hello.world"

def test_mixed_separators():
    assert to_dot_case("Hello_World-Test") == "hello.world.test"

def test_empty_string():
    assert to_dot_case("") == ""

def test_single_word():
    assert to_dot_case("hello") == "hello"

def test_multiple_spaces():
    assert to_dot_case("Hello   World  Test") == "hello.world.test"

def test_type_error():
    with pytest.raises(TypeError):
        to_dot_case(123)

def test_special_characters():
    assert to_dot_case("Hello!World@Test") == "hello.world.test"