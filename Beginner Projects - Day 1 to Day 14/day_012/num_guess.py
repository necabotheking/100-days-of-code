# ---100 Days of Code---
# -- Day 12 Project --

from art import *

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def guessing_game():
    """
    Plays the guessing game

    Inputs:
        None
    
    Returns: Outcome of the game as the user plays
    """
    print("Welcome to the Guessing Game!")
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    # if easy then 10 guesses
    #if hard then 5 guesses


# run the guessing game    
guessing_game()