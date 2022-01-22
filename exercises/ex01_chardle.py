"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730232406"

choice: str = str(input("Enter a 5-character word: "))

if (len(choice)) != int(5):
    print("Error: Word must contain 5 characters")
    exit()

letter: str = str(input("Enter a single character: "))

if (len(letter)) != int(1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + choice)

x: int = 0

if letter == choice[0]:
    print(letter + " found at index 0")
    x = x + 1
if letter == choice[1]:
    print(letter + " found at index 1")
    x = x + 1
if letter == choice[2]:
    print(letter + " found at index 2")
    x = x + 1
if letter == choice[3]:
    print(letter + " found at index 3")
    x = x + 1
if letter == choice[4]:
    print(letter + " found at index 4")
    x = x + 1

if x == 0:
    print("No instances of " + letter + " found in " + choice)
else:
    if x == 1:
        print(str(x) + " instance of " + letter + " found in " + choice)
    else:
        print(str(x) + " instances of " + letter + " found in " + choice)
   