"""Testing the functions in dictionary file."""

__author__ = "730244272"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert() -> None:
    """Testing if it inverts."""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f'}) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_one_pair() -> None:
    """Testing another to see if it inverts."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_empty() -> None:
    """If given empty dict output an empty dict."""
    assert invert({"": ""}) == {"": ""}


def test_favorite_color_frequent() -> None:
    """Seeing if the function returns the most frequent color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_tie() -> None:
    """When there is a tie, print out first value."""
    assert favorite_color({"Marc": "yellow", "Amy": "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow"


def test_favorite_color_empty() -> None:
    """Given an empty dict, return nothing."""
    assert favorite_color({"": ""}) == ""


def test_count_works() -> None:
    """Lets see if it actually counts the str correctly."""
    assert count(["a", "b", "c", "a", "a"]) == {"a": 3, "b": 1, "c": 1}


def test_count_empty_string() -> None:
    """If given empty string, provide empty dict."""
    assert count([]) == {}


def test_count_one_value() -> None:
    """When list is only one value, return one pair."""
    assert count(["a"]) == {"a": 1}