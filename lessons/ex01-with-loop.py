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
i: int = 0

while i < len(choice):
    if letter == choice[i]:
        print(letter + " found at index " + str(i))
        i = i + 1
        x = x + 1
    else:
        i = i + 1
        x = x

if x == 0:
    print("No instances of " + letter + " found in " + choice)
else:
    if x == 1:
        print(str(x) + " instance of " + letter + " found in " + choice)
    else:
        print(str(x) + " instances of " + letter + " found in " + choice)
   