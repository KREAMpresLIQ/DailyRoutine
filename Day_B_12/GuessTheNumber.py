from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """check answer against guess. Returns the number of turns remaining """
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'e' or 'h': ")
    if level == 'e':
        return EASY_LEVEL_TURNS
    elif level == 'h':
        return HARD_LEVEL_TURNS
    else:
        print("Please type 'e' or 'h'")


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"correct {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number!")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again!")


# Track the number of turns and reduce by 1 if they get it wrong.

game()
