# ---100 Days of Code---
# -- Day 9 Project --

import os
from art import *


bidders = {}
auction_end = False

def find_highest_bidder(bidding_dictionary):
    """
    Returns the bidder with the highest bid

    Inputs:
        bidding_dictionary (dict): The dictionary of current bidders
    
    Returns (str): Prints the highest bidder with their amount
    """
    highest_bidder = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = max(bidding_dictionary.values())
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}") 

while not auction_end:
    print(logo)
    print("Welcome to secret auction program\n")

    name = str(input("What is your name: "))
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    finished = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()

    if finished == "no":
        auction_end = True
        find_highest_bidder(bidders)
    elif finished == "yes":
        os.system('clear')
