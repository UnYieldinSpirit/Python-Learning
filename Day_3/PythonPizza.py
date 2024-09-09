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