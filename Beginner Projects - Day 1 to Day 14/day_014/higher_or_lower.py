# ---100 Days of Code---
# -- Day 14 Project --

from art import *
from game_data import *
import random


def check_win(A, B, choice):
    """
    Check's if the player chose the right choice
    
    Inputs:
        A (dict):
        B (dict):
        choice (str):
    
    Returns: True or False
    """
    if choice == "B" and B['follower_count'] > A['follower_count']:
        print("they got it right")
        return True
    elif choice == "A" and A['follower_count'] > B['follower_count']:
        print("they got it right")
        return True
    else:
        print("you got it wrong")
        return False
 
def shift_game(B, game_data_copy):
    """
    Based on if the player won or lost the outcome is given
    
    Inputs:
       game_data_copy (lst): 

    Returns: A and B
    """
    for i in range(len(game_data_copy)):
        if game_data_copy[i] != B:
            continue
        else:
            game_data_copy = game_data_copy[i::]
            A = game_data_copy[0]
            B = game_data_copy[1]
            break
    return A, B


# def random_selection(game_data):
#     """
#     Shuffles the game data 

#     Inputs:
#         game_data (lst): 
    
#     Returns: (dict) A and B 
#     """
#     random.shuffle(game_data)
#     return game_data[0], game_data[1]


def higher_lower():
    """
    Plays the Higher or Lower Game

    Inputs: 
        None

    Returns: Outcome of the game
    """
    game_end = False

    score = 0
    game_data_copy = data[:]
    A = game_data_copy[0]
    B = game_data_copy[1]
    # A, B = random_selection(data)

    while not game_end:
        print(logo)
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        print(f"Your score is currently {score}")
        choice = str(input("Who has more followers? Type 'A' or 'B': ")).upper()
        
        if check_win(A, B, choice) == True:
            score += 1
            # Is a for loop needed to iterate through the list of dicionaries 
            # # and change to the next choice 
            A, B = shift_game(B, game_data_copy)
        else:
            final_score = score
            print(logo)
            print(f"Sorry that's wrong, final score: {final_score}")
            game_end = True
     
        # Things to do:
        # 1. Start the higher lower game and randomly choose A and B
        # 2. If the player guesses correctly B becomes A, then randomly choose B
        # 3. Update the score, tell the player they guessed correctly
        # 4. If the player guesses incorrectly, end the game and show the player 
        #     how many points they received

higher_lower()