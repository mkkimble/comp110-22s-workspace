"""functions skeletons are listed here."""

___author__ = "730244272"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Testing only evens."""
    assert only_evens([]) == []


def test_only_evens_only_odds() -> None:
    """Testing only evens for when only odds are in list."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_one_even() -> None:
    """Testing only evens for when one even is in list."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_multiple_evens() -> None:
    """Testing only evens for when there are multiple evens in list."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_length_zero() -> None:
    """Testing sub for a list that is len 0."""
    a_list: list[int] = []
    assert sub(a_list, 0, 1) == []


def test_sub_a_bigger_than_b() -> None:
    """Testing sub for 'a' value greater than b."""
    assert sub([10, 20, 30, 40], 3, 2) == []


def test_sub_b_less_than_or_zero() -> None:
    """Testing sub for 'b' that is less than or equal to 0."""
    assert sub([10, 20, 30, 40], 1, 0) == []


def test_sub_a_is_negative() -> None:
    """When a is negative."""
    assert sub([10, 20, 30, 40], -1, 2) == [20, 20]


def test_sub_returns_list() -> None:
    """Returns the correct indices."""
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_sub_end_greater_list() -> None:
    """If end index is greater than len of list."""
    assert sub([1, 2, 3, 4], 1, 5) == [2, 4]


def test_concat() -> None:
    """Testing to add 2nd list to 1st list."""
    assert concat([10, 20], [30, 40]) == [10, 20, 30, 40]


  
        
   
