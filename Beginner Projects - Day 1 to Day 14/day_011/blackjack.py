# ---100 Days of Code---
# -- Day 11 Project --

from art import *
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  

def deal_card(cards):
    """
    Deals the user and the computer 2 cards each

    Inputs: (lst) list of cards

    Returns: (lst) lst of dealer and user cards
    """
    user_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)
    return user_cards, dealer_cards

def calculate_score(player_hand):
    """
    Calculates the score 
    
    Inputs: (lst) list of cards

    Returns: (int) score
    """
    if sum(player_hand) == 21 and len(player_hand) == 2:
        score = 0
    else:
        score = sum(player_hand)
    return score

play_game = input("Do you want to play a game of blackjack? Type 'y' or 'n' \n:")
game_end = True

if play_game == 'y':
    game_end = False
    while not game_end:
        print(logo)


