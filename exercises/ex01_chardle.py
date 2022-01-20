"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730232406"

guess: str = str(input("Enter a 5-character word: "))

if (len(Guess)) != int(5):
    print("Error: Word must contain 5 characters")
    exit()

letter: str = str(input("Enter a single character: "))

if (len(letter)) != int(1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + guess)

x: int = 0

if letter == guess[0]:
    print(letter + " found at index 0")
    x = x + 1
if letter == guess[1]:
    print(letter + " found at index 1")
    x = x + 1
if letter == guess[2]:
    print(letter + " found at index 2")
    x = x + 1
if letter == guess[3]:
    print(letter + " found at index 3")
    x = x + 1
if letter == guess[4]:
    print(letter + " found at index 4")
    x = x + 1

if x == 0:
    print("No instances of " + letter + " found in " + guess)
else:
    if x == 1:
        print(str(x) + " instance of " + letter + " found in " + guess)
    else:
        print(str(x) + " instances of " + letter + " found in " + guess)
   