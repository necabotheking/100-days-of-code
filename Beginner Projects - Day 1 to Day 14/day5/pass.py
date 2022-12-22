# ---100 Days of Code---
# -- Day 5 Project --

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator.")

letter_int = int(input("How many letters would you like in your password?\n"))
while letter_int > len(letters):
    letter_int = int(input("Please choose a valid number of letters for your password\n"))
  

symbol_int = int(input("How many symbols would you like?\n"))
while symbol_int > len(symbols):
    symbol_int = int(input("Please choose a valid number of symbols for your password\n"))


num_int = int(input("How many numbers would you like?\n"))
while num_int > len(numbers):
    num_int = int(input("Please choose a valid number of numbers for your password\n"))


password = []
for _ in range(letter_int):
    letter_selection = random.randint(0, len(letters)-1)
    password += letters[letter_selection]

for _ in range(symbol_int):
    symbol_selection = random.randint(0, len(symbols)-1)
    password += symbols[symbol_selection]

for _ in range(num_int):
    num_selection = random.randint(0, len(numbers)-1)
    password += numbers[num_selection]

print(f"Here is your password: {''.join(password)}")

random.shuffle(password)
print(f"Here is a shuffled password: {''.join(password)}")
