"""EX03 - Structured Wordle."""

__author__ = "730232406"


def contains_char(secret: str, letter: str) -> bool:
    """Finds a single character at any index of the secret."""
    assert len(letter) == 1

    i: int = 0

    while i < len(secret):
        if letter == secret[i]:
            return True
        else:
            i += 1
    
    return False


def emojified(guess: str, secret: str) -> str:
    """Will return string of emojis whose color codifies a match."""
    assert len(guess) == len(secret)

    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    
    x: int = 0
    output: str = ""

    while x < len(secret):
        if guess[x] == secret[x]:
            output += green_box
            x += 1
        else:
            contains_char(secret, guess[x])
            
            scan: bool = contains_char(secret, guess[x])

            if scan == (True):
                output += yellow_box
            else:
                output += white_box
            x += 1
    
    return (output)


def input_guess(exp_len: int) -> str:
    """Prompts user for guess of specific length."""
    guess: str = input(f"Enter a {exp_len} character word: ")

    while len(guess) != exp_len:
        guess = input(f"That wasn't {exp_len} chars! Try again: ")

    return (guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    guess: str = ""
    secret: str = "codes"
    result: bool = False

    while turn < 7 and result == (False):
        print(f"=== Turn {turn}/6 ===")

        input_guess(len(secret))
        guess = input_guess(len(secret))

        emojified(guess, secret)
        Hint: str = emojified(guess, secret)
        print(Hint)

        if guess == secret:
            result = bool(True)
        else:
            turn += 1

    if result == (True):
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()