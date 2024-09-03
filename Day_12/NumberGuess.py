import random

# lets the computer choose a random number to start
comp_num = random.choice(range(0,101))
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
life = 0
win = False

def set_lives(mode):
    """Initiates the beginning portions of the game, giving the player the necessary amount of lives that they need based on the selected difficulty"""
    global life
    if mode == "hard":
        life = 5
    elif mode == "easy":
        life = 10

def lose_life():
    """Removes a life from the player's overall remaining lives"""
    global life
    life -= 1
    print(f"Lives remaining: {life}")

def invalid_entry(entry):
    """Verifies that the user is entering an acceptable entry. If not then they will be prompted to enter the acceptable inputs until they do (recursive). Returns the user's input.
    """
    if entry != "hard" and entry != "easy":
        entry = input("Invalid Entry. Try again! 'easy' or 'hard': ").lower()
        entry = invalid_entry(entry)
    return entry

def invalid_play_again(entry):
    """Verifies that the user is entering an acceptable entry. If not then they will be prompted to enter the acceptable inputs until they do (recursive). Returns the user's input.
    """
    if entry != "y" and entry != "n":
        entry = input("Invalid Entry. Try again! 'y' or 'n': ").lower()
        entry = invalid_play_again(entry)
    return entry

def check(num):
    """Checks to see where the number guess is in respect to the computer's selected number and informs the user. Also verifies if the player won or not
    """
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

def restart():
    """Resets the parameters of the game and starts the game, so the user can replay the game without having to re-run the code at all
    """
    global comp_num
    global win
    global difficulty

    comp_num = random.choice(range(0, 101))
    win = False
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    game()


def endgame():
    """Reports to the user whether they won or lost the game. Also asks the player if they would like to play again. Where it then begins the process to restart the game"""
    if life == 0:
        print(f"You Lose! The number was {comp_num}")
    else:
        print(f"YOU WIN! The number was {comp_num}")

    play_again = input("Play Again? (y/n) ").lower()
    if play_again != "y" and play_again != "n":
        play_again = invalid_play_again(play_again)
    if play_again == "y":
        restart()
    elif play_again == "n":
        print("Thank you for playing!")

def game():
    """Main game logic and innerworkings"""
    global difficulty
    
    # if statement that signals the invalid entry function if the difficulty selected was not a valid entry
    if difficulty != "easy" and difficulty != "hard":
        difficulty = invalid_entry(difficulty)

    set_lives(difficulty)

    # continuous loop that runs until the player runs out of lives and lose or until they guess the number correctly and win
    while life > 0 and win != True:
        guess = int(input("Guess a number: "))
        check(guess)

    # Initiates the endgame section
    endgame()

game()