# todo: work out how much they need to pay based on their size choice

# todo: work out how much to add to their bill based on their pepperoni choice.

# todo: work out their final amount based on where they want extra cheese.

# S - 15, M - 20, L - 25
# Pepp (S) - +2, Pepp (M or L) - +3,
# Extra Cheese - +1

print("Welcome to the Python Pizza Shop!")
size = input("What size pizza would you like to order? S, M, or L: ")
pepperoni = input("Would you like pepperoni on that pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else: # Large pizza
    bill = 25


if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}.")