# ---100 Days of Code---
# -- Day 12 Project --

from art import *
import random

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
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # if easy then 10 guesses
    #if hard then 5 guesses
    num_guess = random.randint(0,100)
    print(f"The number is {num_guess}")
    if difficulty == "easy":
        guesses = 10
    else:
        guesses = 5

    for turn in reversed(range(1, guesses + 1)):
        # For each turn do this
        print(f"You have {turn} attempts remaining to guess the number")
        user_guess = int(input("Please guess a number: "))
        if user_guess == num_guess:
            print("You got it right!")
            quit()
        elif user_guess > num_guess:
            print("Too High!")
        else:
            print("Too Low!")

# run the guessing game    
guessing_game()