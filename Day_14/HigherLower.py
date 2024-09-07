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
    print(art.logo)

def vs():
    print(art.vs)

def competitors():
    """Sets the two options that are used for the game"""
    global choice1
    global choice2
    num1 = random.randrange(0, len(gamedata.data) - 1)
    num2 = random.randrange(0, len(gamedata.data) - 1)
    while num1 == num2:
        num1 = random.randrange(0, len(gamedata.data) - 1)     

    choice1 = gamedata.data[num1]       
    choice2 = gamedata.data[num2]

def loss():
    """Sets the loss condition to true to initiate the endgame function"""
    global loss_condition
    loss_condition = True

def compare(user_input):
    """Compares the two options against each other to decide which one has the most followers and which choice is the correct choice as a result"""
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
    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    if 'A' != user != 'B':
        print("That is not a valid choice")
        user = user_choice_game()
        return user
    else:
        return user

def user_choice_play_again():
    user = input("Play Again? Type 'Y' or 'N': ").upper()
    if 'Y' != user != 'N':
        print("That is not a valid choice")
        user = user_choice_play_again()
        return user
    else:
        return user

def send_options(info):
    return f"{info['name']}, a {info['description']}, from {info['country']}"

def endgame():
    """Initiates the game ending when the player loses"""
    global streak
    print(f"You got {streak} correct!")

def game():
    title()
    competitors()
    print(f"Choice A: {send_options(choice1)}")
    vs()
    print(f"Choice B: {send_options(choice2)}")
    compare(user_choice_game())

print(game_prompt)
while loss_condition == False:
    game()
endgame()