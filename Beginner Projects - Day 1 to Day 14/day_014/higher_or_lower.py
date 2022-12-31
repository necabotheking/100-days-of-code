# ---100 Days of Code---
# -- Day 14 Project --

from art import *
from game_data import *


def check_win():
    """
    Check's if the player chose the right choice
    
    Inputs:
        [Inputs Here]
    
    Returns:
    """
    pass
 
def outcome():
    """
    Based on if the player won or lost the outcome is given
    
    Inputs:
        [Inputs Here]

    Returns:
    """
    pass


def higher_lower():
    """
    Plays the Higher or Lower Game

    Inputs: 
        None

    Returns: Outcome of the game
    """
    game_end = False

    score = 0
    # A = data[]
    # B = data[]

    while not game_end:
        print(logo)
        print("Compare A: ")
        print(vs)
        print("Against B:")

        print(f"Your score is currently {score}")
        choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        #if check_win(choice) == True:
     
        # Things to do:
        # 1. Start the higher lower game and randomly choose A and B
        # 2. If the player guesses correctly B becomes A, then randomly choose B
        # 3. Update the score, tell the player they guessed correctly
        # 4. If the player guesses incorrectly, end the game and show the player 
        #     how many points they received

higher_lower()