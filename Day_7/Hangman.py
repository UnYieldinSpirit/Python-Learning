import random

word_bank = ["peanut", "alphabet", "caramel", "gideon", "flabbergasted", "apple", "beanie", "hyperthermia", "summer", "rapper", "python", "hanger", "serendipity", "problematic", "charismatic", "stupendous", "aromatherapy", "gorgeous", "leprechaun", "idiosyncrasy", "cyanide", "organic", "agoraphobic"]
comp_word = ""
reveal_list = []
comp_word_list = []
guessed_letters = []
num_guesses = 8
correct = False # variable that tracks if the user's guess is correct
game_won = False
play_again = True

def set_word():
    global comp_word
    comp_word = random.choice(word_bank)

# function that sets the list that handles displaying the revealed letters in the word. Ensures that the lengths are the same
def set_reveal_list():
    global reveal_list
    reveal_list = []
    for space in range(len(comp_word)):
        reveal_list.append("-")

def set_comp_word_list():
    global comp_word_list
    comp_word_list = []
    for char in comp_word:
        comp_word_list.append(char)

def reset_guessed_letters():
    global guessed_letters
    guessed_letters = []

def check():
    if reveal_list == comp_word_list:
        return True
    else:
        return False

def reset_game(): # "global" allows the function the ability to interact with the variables outside of the scope of the function
    global comp_word
    global comp_word_list
    global reveal_list
    global num_guesses
    global game_won
    global correct
    global main_counter

    num_guesses = 8
    correct = False # variable that tracks if the user's guess is correct
    game_won = False
    main_counter = 0
    reset_guessed_letters()
    set_word()
    set_comp_word_list()
    set_reveal_list()

    
while play_again == True:
    reset_game()

    # print(comp_word)
    # print(comp_word_list)
    # print(reveal_list)

    print(f"Welcome to Hangman! You get a total of {num_guesses} incorrect guesses before you lose...\nDuplicate guesses do not count! Good luck")
    main_counter = 0
    while num_guesses > 0 and game_won == False:
        correct = False
        print(f"Number of guesses left: {num_guesses}")

        if main_counter == 0:
            print(f"{len(comp_word)}-letter word")
        print(reveal_list)

        if main_counter != 0:
            print(f"Here are all of the letters that you have already guessed:\n{guessed_letters}")
        
        user_guess = input("Guess a letter: ").lower()

        counter = 0
        for char in comp_word_list:
            if user_guess == char:
                correct = True
                reveal_list[counter] = user_guess
                if user_guess not in guessed_letters:
                    guessed_letters.append(user_guess)
                else:
                    print("You already guessed that letter... Try another one!")
            counter += 1

        if correct == False:
            print(f"{user_guess} is not in this word...")
            if user_guess not in guessed_letters:
                guessed_letters.append(user_guess)
                num_guesses -= 1
            else:
                print("You already guessed that letter. Try again.")
        
        if check() == True:
            game_won = True

        main_counter += 1

    if num_guesses == 0 and game_won == False:
        print(f"You Lose!\nThe word was: {comp_word}...")
    else:
        print(f"You win!\nThe word was: {comp_word}!")

    user_input = input("Play Again? (y/n) ").lower()

    if user_input == "y":
        play_again = True
    else:
        play_again = False
print("Thanks for playing!")