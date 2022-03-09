"""Playing around with dictionarys."""

__author__ = "730244272"


def invert(inverts: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    # I am literally trying random things at this point, hoping it works
    inv_inverts = dict(zip(inverts.values(), inverts.keys()))
    return inv_inverts


def favorite_color(a: dict[str, str]) -> str:
    """Returns the string with the most popular color, if tie, returns first color."""
    final = list(a.values())
    # This is going to put the values in a list
    number = max(final, key=final.count)
    # This will found the most frequently occuring value and output it
    return number

   
def count(given: list[str]) -> dict[str, int]:
    """Given a list, return the str with its accompanying frequency."""
    counting = {}
    # Giving an empty dictionary to build up the str, ints
    for items in given:
        if items in counting.keys():
            # Should show us if it is present and if it is, will add to its frequency.
            counting[items] += 1
        else:
            # If the item is not present in the list again then it will just print out one.
            counting[items] = 1
    return counting 
    # Gives the dictionary with the str values as they keys and then the ints as the values.
