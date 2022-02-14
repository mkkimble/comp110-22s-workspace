"""Developemnt of Wordle game."""

__author__ = "730244272"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search: str, character: str) -> bool:
    """True if character is in search, false otherwise."""
    assert len(character) == 1
    # right now we are simply searching for one character
    i: int = 0
    while i < len(search):
        if search[i] == character:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Strings of equal length, codify the boxes to yellow or white."""
    assert len(guess) == len(secret)
    i: int = 0
    resulting_emoji: str = ""
    while i < len(secret):
        if contains_char(secret, guess[i]) is False:
            resulting_emoji: str = resulting_emoji + WHITE_BOX
        else: 
            if secret[i] == guess[i]:
                resulting_emoji: str = resulting_emoji + GREEN_BOX
            else:
                resulting_emoji: str = resulting_emoji + YELLOW_BOX
        i += 1
    return resulting_emoji
    # now we have a string of emojis


def input_guess(expected: int) -> str:
    """Given an integer, user inputs guess of that length."""
    # continue prompting until user enters word of the correct length
    how_long: str = input(f"Enter a {expected} character word: ")
    while len(how_long) != expected:
        if len(how_long) != expected:
            how_long: str = input(f"That wasn't {expected} chars! Try again: ")
        else: 
            if len(how_long) == expected:
                print(how_long)
    return how_long
    #  now we have associated word with length


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    # putting all the other functions in this function
    secret_word: str = "codes"
    i: int = 1
    turn: int = 6
    while i < turn:
        print(f"=== Turn {i}/6 ===")
        how_long: str = input(f"Enter a {len(secret_word)} character word: ")
        if how_long != secret_word:
            print(emojified(how_long, secret_word))
        else:
            if how_long == secret_word:
                print(emojified(how_long, secret_word)) 
                print(f"You won in {i}/6 turns!")
                exit()
                
        i += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()