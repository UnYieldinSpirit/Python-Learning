import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+']
new_letters = []

# identifies the number of letters, symbols and numbers
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# variables that hold the characters randomly selected from the lists
sel_numbers = ""
sel_symbols = ""
sel_letters = ""

i = 0 # while condition

# while loop that handles the process of parsing the list to select a character that will be stored in the 'selected' variables
while i != nr_letters:
    sel_letters += random.choice(letters)
    i += 1

i = 0 # reset while condition
while i != nr_symbols:
    sel_symbols += random.choice(symbols)
    i += 1

i = 0 # reset while condition
while i != nr_numbers:
    sel_numbers += random.choice(numbers)
    i += 1

# combines the selected characters to form the password
password = sel_letters + sel_numbers + sel_symbols # find a way to concatenate the segmented passwords together
print(password)