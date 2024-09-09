"""DRY CODE IS BETTER THAN WET CODE
Don't
Repeat
Yourself

We
Enjoy
Typing
"""

import random
import art
import gamedata

correct_choice = "A"
streak = 0 # used to track how many the player gets correct'
loss_condition = False
choice1 = {}
choice2 = {}

game_prompt = """This is the way that the game is run. Two choices will be given to you.
You are tasked with deciding which one has the higher amount of followers. 
Get it right and you move on, get it wrong and you lose your streak."""

def title():
    """prints the HigherLower art title"""
    print(art.logo)

def vs():
    """prints the HigherLower vs art"""
    print(art.vs)

def reset_params():
    """resets the parameters of the game to ensure that the game restarts"""
    global streak
    global loss_condition
    streak = 0
    loss_condition = False

def competitors():
    """sets the two options that are used for the game"""
    global choice1
    global choice2
    num1 = random.randrange(0, len(gamedata.data) - 1)
    num2 = random.randrange(0, len(gamedata.data) - 1)
    while num1 == num2:
        num1 = random.randrange(0, len(gamedata.data) - 1)     

    choice1 = gamedata.data[num1]       
    choice2 = gamedata.data[num2]

def loss():
    """sets the loss condition to true to initiate the endgame function"""
    global loss_condition
    loss_condition = True

def compare(user_input):
    """compares the two options against each other to decide which one has the most followers and which choice is the correct choice as a result"""
    global loss
    global correct_choice
    global streak
    if choice1["follower_count"] > choice2["follower_count"]:
        correct_choice = "A"
    elif choice1["follower_count"] < choice2["follower_count"]:
        correct_choice = "B"
    if correct_choice == user_input:
        print("CORRECT!")
        streak += 1
    else:
        print("INCORRECT")
        loss()

def user_choice_game():
    """ensures that the user inputs are valid"""
    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    if 'A' != user != 'B':
        print("That is not a valid choice")
        user = user_choice_game()
        return user
    else:
        return user

def user_choice_play_again():
    """ensures that the user inputs are valid"""
    user = input("Play Again? Type 'Y' or 'N': ").upper()
    if 'Y' != user != 'N':
        print("That is not a valid choice")
        user = user_choice_play_again()
        return user
    else:
        return user

def send_options(info):
    """populates the choice with the appropriate information"""
    return f"{info['name']}, a {info['description']}, from {info['country']}"

def endgame():
    """Initiates the game ending when the player loses"""
    global streak
    print(f"You got {streak} correct!")
    if user_choice_play_again() == 'Y':
        reset_params()
        game()
    else:
        print(f"Thank you for playing! Let's see if you can get a higher streak than {streak} next time!")

def game():
    """contains all of the functionality of the game"""
    global loss_condition
    while loss_condition == False:
        title()
        competitors()
        print(f"Choice A: {send_options(choice1)}")
        vs()
        print(f"Choice B: {send_options(choice2)}")
        compare(user_choice_game())
    endgame()

print(game_prompt)
game()