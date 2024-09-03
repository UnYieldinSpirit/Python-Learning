import random

# need a random number
# check systems to tell the player whether they are above or below the number

# lets the computer choose a random number to start
comp_num = random.choice(range(0,101))
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
life = 0
win = False

def set_lives(mode):
    global life
    if mode == "hard":
        life = 5
    elif mode == "easy":
        life = 10

def lose_life():
    global life
    life -= 1
    print(life)

def invalid_entry(entry):
    if entry != "hard" and entry != "easy":
        entry = input("Invalid Entry. Try again! 'easy' or 'hard': ").lower()
        entry = invalid_entry(entry)
    return entry

def invalid_number(entry):
    if type(entry) != int:
        entry = input("That is not an integer (whole number). Try again! ")
        entry = invalid_entry(entry)

def check(num):
    global comp_num
    global win
    if num > comp_num:
        print("Lower")
        lose_life()
    elif num < comp_num:
        print("Higher")
        lose_life()
    else:
        print("THAT'S RIGHT!")
        win = True

if difficulty != "easy" and difficulty != "hard":
    difficulty = invalid_entry(difficulty)

set_lives(difficulty)

while life > 0 and win != True:
    guess = int(input("Guess a number: "))
    check(guess)

if life == 0:
    print(f"You Lose! The number was {comp_num}")
else:
    print(f"YOU WIN! The number was {comp_num}")