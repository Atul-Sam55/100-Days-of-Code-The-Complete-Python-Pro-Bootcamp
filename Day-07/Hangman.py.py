import random
from hangman_words import word_list
from hangman_arts import stages, logo

lives = 6
game_over = False
correct_letters = []

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create placeholder
display = "_" * word_length
print("Word to guess:", display)

while not game_over:
    print(f"\n****************** {lives}/6 LIVES LEFT ******************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")

    # Build display
    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print("Word to guess:", display)

    # Wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\n***************** IT WAS '{chosen_word}'! YOU LOSE *****************")

    # Win condition
    if "_" not in display:
        game_over = True
        print("\n***************** YOU WIN *****************")

    print(stages[lives])
