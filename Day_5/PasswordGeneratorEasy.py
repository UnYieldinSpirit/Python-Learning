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

# for loop that handles the process of parsing the list to select a character that will be stored in the 'selected' variables

for char in range(0, nr_letters):
    sel_letters += random.choice(letters)

for char in range(0, nr_symbols):
    sel_symbols += random.choice(symbols)

for char in range(0, nr_numbers):
    sel_numbers += random.choice(numbers)

# combines the selected characters to form the password
password = sel_letters + sel_symbols + sel_numbers # find a way to concatenate the segmented passwords together
print(password)