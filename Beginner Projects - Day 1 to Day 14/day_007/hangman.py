# ---100 Days of Code---
# -- Day 7 Project --

import random

from hangman_words import *
from hangman_art import *

print(logo)
print("Welcome to Hangman!\n")

chosen_word = random.choice(word_list)
#print(f"The word is {chosen_word}")

# create the blank game board
game_display = len(chosen_word) * ["_"]

game_lives = 6
game_end = False
while not game_end:

    guess = str(input("Please guess a letter:\n")).lower()

    # check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            game_display[position] = guess

    if guess not in chosen_word:
        print("\nOops Wrong Guess")
        game_lives -= 1
        if game_lives == 0:
            game_end = True
            print("You lose!")
            print(f"The word is {chosen_word}")

    print(f"{' '.join(game_display)}")

    if "_" not in game_display:
        game_end = True
        print("You win!")

    print(stages[game_lives])