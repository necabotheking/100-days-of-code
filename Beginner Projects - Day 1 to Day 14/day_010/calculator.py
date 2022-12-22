# ---100 Days of Code---
# -- Day 10 Project --

from art import *
import os

# calculator functions below  

# add
def add(num1, num2):
    return num1 + num2

# subtract
def sub(num1, num2):
    return num1 - num2

# divide
def div(num1, num2):
    return num1 / num2

# multiply
def mult(num1, num2):
    return num1 * num2

operations_dict = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mult
}


def calculator():
    """
    Multiplies, Divides, Subtracts, and Adds
    
    Inputs: None

    Returns: (float) Answer to the selected operation
    """
    print(logo)

    num1 = float(input("What is the first number?: \n"))
    for symbol in operations_dict:
        print(symbol)
    continue_operation = True

    while continue_operation:
        operation = input("What operation would you like to perform?: \n")
        while operation not in operations_dict:
            operation = input("What operation would you like to perform?: \n")

        num2 = float(input("What is the second number?: \n"))
        calculator_operation = operations_dict[operation]
        answer = calculator_operation(num1, num2)
        print(f" {num1} {operation} {num2} = {answer}")

        finished = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or anything else to quit: \n")
        if finished == "y":
            num1 = answer
        elif finished == 'n':
            continue_operation = False
            os.system('clear')
            calculator()
        else:
            continue_operation = False
            os.system('clear')

calculator()
