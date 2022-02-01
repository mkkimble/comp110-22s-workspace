"""Wordle game--Python"""

__author__ = 730244272

secret_word: str = "python"
word_size: int = len(secret_word)
guess: str = input(f"What is your {word_size}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# was unsure if i was supposed to keep the named constants fully capitalized

i: int = 0
# for the index #

while len(secret_word) != len(guess):
    guess: str = input(f"That was not {word_size} letters! Try again: ")
   
if guess == secret_word:
    print("Woo! You got it!")
    print(word_size * GREEN_BOX)
else: 
    if len(guess) == len(secret_word):
        while i < len(secret_word):
            if guess[i] == secret_word[i]:
                print(GREEN_BOX)
            else:
                if guess[i] in secret_word:
                    print(YELLOW_BOX)
                    # i did not understand how to do the boolean method as described, so I just did this instead.
                else:
                    print(WHITE_BOX)
            i += 1
            # adding 1 to go through the indices of the guess and the secret word
# i really don't know how to put the emojis on the same line. I'm going crazy.
        print("Not quite. Play again soon!")
