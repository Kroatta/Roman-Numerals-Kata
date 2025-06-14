from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("5") == 5

def test_two_numbers():
    assert add("1,2") == 3
def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_and_comma_mix():
    assert add("1\n2,3") == 6
def test_custom_delimiter():
    assert add("//;\n1;2") == 3
import pytest

def test_negative_number_raises_exception():
    with pytest.raises(ValueError, match="negatives not allowed: -1"):
        add("1,-1,2")

def test_multiple_negatives_raise_all():
    with pytest.raises(ValueError, match="negatives not allowed: -1, -4"):
        add("1,-1,2,-4")
def test_ignore_number_above_1000():
    assert add("2,1001") == 2

def test_include_1000():
    assert add("1000,1") == 1001
def test_delimiter_with_multiple_characters():
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
        assert add("//[*][%]\n1*2%3") == 6

def test_multiple_long_delimiters():
        assert add("//[***][##][@@]\n1***2##3@@4") == 10