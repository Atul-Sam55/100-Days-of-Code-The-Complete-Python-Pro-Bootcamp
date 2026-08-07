from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")  # Remove after testing

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if guess == answer:
            break

        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        else:
            print("Guess again.")


game()
