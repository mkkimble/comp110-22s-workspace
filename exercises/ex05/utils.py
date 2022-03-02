"""Titled Utils; implementing function skeletons and implementations."""

__author__ = "730244272"


def only_evens(xs: list[int]):
    """Returning only evens from a list."""
    even_numbers = []
    # An empty list above
    for even in xs:
        if even % 2 == 0:
            even_numbers.append(even)
    return even_numbers
    # Should now return all of the even numbers after it goes through the list.


def sub(a_list: list[int], a: int, b: int):
    """Returning a sublist from the entire list."""
    # This should return the numbers at the indices wanted.
    indices = [a_list[a], a_list[b]]
    if len(a_list) == 0:
        return []
    else:
        if a > len(a_list):
            return []
        else:
            if a > b:
                return []
            else:
                if a < b:
                    if b < len(a_list):
                        if b >= 0:
                            return indices
                        else: 
                            return []


def concat(one_list: list[int], two_list: list[int]):
    """A list that combines both of the lists together."""  
    for x in two_list: 
        one_list.append(x)
    return one_list
    # Looks simple but test passed to add the lists together.