# ---100 Days of Code---
# -- Day 9 Project --
import os
from art import *


bidder_dict = {}
auction_end = False

while not auction_end:
    print(logo)
    print("Welcome to secret auction program\n")

    name = str(input("What is your name: "))
    bid = int(input("What is your bid?: $"))

    bidder_dict[name] = bid


    done = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower
    #below clears the console after the last entry
    if done == 'yes':
        print("The winner is [name] with a bid of [price]")
        auction_end = True
    else:
        os.system('clear')