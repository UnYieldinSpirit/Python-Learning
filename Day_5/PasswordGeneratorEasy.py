import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '(', ')', '*', '+']
new_letters = []
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

sel_numbers = ""
sel_symbols = ""
sel_letters = ""
i = 0

while i != nr_letters:
    sel_letters += random.choice(letters)
    i += 1

print(sel_letters)

i = 0 # reset while condition
while i != nr_symbols:
    sel_symbols += random.choice(symbols)
    i += 1

print(sel_symbols)

i = 0 # reset while condition
while i != nr_numbers:
    sel_numbers += random.choice(numbers)
    i += 1

print(sel_numbers)

password # find a way to concatenate the segmented passwords together
print(password)

# for the hard part where the password has any order of numbers, put all of the lists into one list and then use random() with range() to specify which list is being referenced at certain times.