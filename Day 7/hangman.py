import random
from os import system
import hangman_art
import hangman_words

# Print hangman logo
print(hangman_art.logo)
# Generate the word for the game, capture the word length, and set lives to 6
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
lives = 6

# Create an empyt list called display
display = []

# Populate display list with underscores for the length of the chosen word
for letter in chosen_word:
    display.append("_")

# Empty list to remember user guesses
all_guesses = []

# Create a variable to determine if the game is over
game_over = False

# Set loop until user wither win's the game or exhausts their guesses.
while not game_over:
# Take user's letter guess and add to all_guesses list
    guess = input("Guess a letter: ").lower()
    # Clear the screen
    system('clear')
    if guess in all_guesses:
        print(f"You have already guessed {guess}.")
        print(f"{' '.join(display)}")
    else:
        all_guesses += guess
        # Iterate through the chosen word and test if the guess matches letters in the chosen word. 
        # If the letters match, set the same position in display to the guess.
        for i in range(word_len):
            if guess == chosen_word[i]:
                display[i] = guess
        # If the user guesses a letter not in the chosen word, reduce lives by 1. 
        # If user runs out of lives, game is over and user loses.
        if guess not in chosen_word:
            print(f"You guessed {guess}. That is not in the word and you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
        # If display's characters have all been guess, user has won the game.
        if "_" not in display:
            game_over = True
            print("You win!")
    
    print(hangman_art.stages[lives])