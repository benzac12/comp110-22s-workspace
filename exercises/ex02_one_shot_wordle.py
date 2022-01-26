"""EX02 - One-Shot Wordle."""

__author__ = 730232406

secret: str = ("python")
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

i: int = 0
output: str = ""

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while i < len(secret):
    if guess[i] == secret[i]:
        output = output + green_box
        i = i + 1
    else:
        chance: bool = False
        x: int = 0
        while chance != (True) and x < len(secret):
            if guess[i] == secret[x]:
                chance = bool(True)
            else:
                x = x + 1
       
        if chance == bool(True):
            output = output + yellow_box
        else:
            output = output + white_box
        i = i + 1

print(output)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")