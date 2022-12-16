# ---100 Days of Code---
# -- Day 2 Project --

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? \n$"))

tip = int(input("What percentage would you like to tip? 10, 15, or 20? \n"))

people = int(input("How many people will split the bill? \n"))

# Each person will pay (bill/people) * tip
# IF the bill was $150.00 with 5 people and a 12% tip.
# (150.00/5) * 1.12

assert people > 0, "Sorry, number of people must be 1 or more"
# edit to correct the assert statement to create a more gentle error within
# the program
 
final_price = (bill/people) *  (1 + (tip * 0.01))

print("Each person should pay %.2f" % final_price)