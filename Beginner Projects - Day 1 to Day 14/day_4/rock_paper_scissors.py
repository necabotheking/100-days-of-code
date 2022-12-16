# ---100 Days of Code---
# -- Day 4 Project --

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

player_1 = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors." + "\n"))
player_2 = random.randint(0, len(game_images) - 1)

while player_1 != 0 and player_1 != 1 and player_1!= 2:
    player_1= int(input("Try again. \nType 0 for Rock, 1 for Paper or 2 for Scissors." + "\n"))
print("\n")

print("You played")
print(game_images[player_1])

print("Computer played")
print(game_images[player_2])


if player_1 == 0:
    if player_2 == 0:
        print("It's a tie!")
    elif player_2 == 1:
        print("You lose!")
    else:
        print("You win!")

if player_1 == 1:
    if player_2 == 0:
        print("You win!")
    elif player_2 == 1:
        print("It's a tie!")
    else:
        print("You lose!")

if player_1 == 2:
    if player_2 == 0:
        print("You lose!")
    elif player_2 == 1:
        print("You win!")
    else:
        print("You lose!")
