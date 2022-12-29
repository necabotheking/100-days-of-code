# ---100 Days of Code---
# -- Day 11 Project --

from art import *
import random
import os

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

def deal_card():
    """
    Deals a card 

    Inputs: 
        None

    Returns: (int) card value
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
    card = random.choice(cards)
    return card

def calculate_score(player_hand):
    """
    Calculates the score 
    
    Inputs: 
        (lst) list of cards

    Returns: (int) score
    """
    if sum(player_hand) == 21 and len(player_hand) == 2:
        score = 0
    elif 11 in player_hand and sum(player_hand) > 21:
        player_hand.remove(11)
        player_hand.append(1)
        score = sum(player_hand)
    else: 
        score = sum(player_hand)
    return score

def compare_score(user_score, computer_score):
    """
    Compares the game scores of the user and the computer

    Inputs: 
        user_score (lst): list of cards
        computer_score (lst): list of cards

    Returns: (str) game outcome 
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """
    Plays the blackjack game

    Input:
        None
    
    Returns: game outcome
    """
    print(logo)

    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())  
        
    while not game_over:  
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(dealer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {dealer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to draw another card, 'n' to pass: ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        dealer_cards.append(deal_card())
        computer_score = calculate_score(dealer_cards) 

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {dealer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()
