"""Wordle game--Python."""

__author__ = "730244272"

secret_word: str = "sake"
word_size: int = len(secret_word)
# instead of using numbers, this will serve as a shortcut for the secret word length. even if changed, the program should modify itself
guess: str = input(f"What is your {word_size}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# was unsure if i was supposed to keep the named constants fully capitalized

i: int = 0
# for the index #, starting at 0
resulting_emoji: str = " "
# keeps track of the emoji that results; is an empty string

while len(secret_word) != len(guess):
    guess: str = input(f"That was not {word_size} letters! Try again: ")
   
if guess == secret_word:
    print("Woo! You got it!")
    print(word_size * GREEN_BOX)
else: 
    if len(guess) == len(secret_word):
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                resulting_emoji: str = resulting_emoji + GREEN_BOX
            else:
                if guess[i] in secret_word:
                    resulting_emoji: str = resulting_emoji + YELLOW_BOX
                    # adding onto resulting emoji string keeps the emoji string together
                else:
                    resulting_emoji: str = resulting_emoji + WHITE_BOX
            i += 1
            # adding 1 to go through the indices of the guess and the secret word
        print(resulting_emoji)
        # prints out an emoji string for all of the letters in the word.
        print("Not quite. Play again soon!")
