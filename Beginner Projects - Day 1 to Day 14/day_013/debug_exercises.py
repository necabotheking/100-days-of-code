# ---100 Days of Code---
# -- Day 13 Project --

# Debug the code below: Odd or Even

'''
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
'''

# Changed = to ==, to check if a number % 2 is 0

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Debug the code below: Leap Year

'''
year = input("Which year do you want to check")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
'''

# Added int() to year input to change the inputted value to an integer
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")


# Debug the code below: FizzBuzz

'''
for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])       
'''

# Changed 'or' to 'and'
# Changed if statements to elif

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])  