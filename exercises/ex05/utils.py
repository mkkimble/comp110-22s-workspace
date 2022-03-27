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


def sub(a_list: list[int], start_index: int, end_index: int):
    """Returning a sublist from the entire list."""
    second_start_index: int = abs(start_index)
    end_index_two: int = len(a_list)

    if a_list == []:
        return []
    if start_index < 0 and start_index < end_index and start_index < len(a_list) and end_index > 0:
        start_index = second_start_index
        return [a_list[second_start_index], a_list[end_index - 1]]
    if start_index < end_index and start_index < len(a_list) and end_index > 0:
        if end_index > len(a_list):
            end_index = end_index_two
        return [a_list[second_start_index], a_list[end_index - 1]]
    else:
        return []


def concat(one_list: list[int], two_list: list[int]):
    """A list that combines both of the lists together."""  
    for x in two_list: 
        one_list.append(x)
    return one_list
    # Looks simple but test passed to add the lists together.