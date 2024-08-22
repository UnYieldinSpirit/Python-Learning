import random

word_bank = ["peanut", "alphabet", "caramel", "gideon", "flabbergasted"]
comp_word = random.choice(word_bank)
comp_word_list = []
reveal_list = []
guessed_letters = []
num_guesses = 5
correct = False # variable that tracks if the user's guess is correct
game_won = False

# function that sets the list that handles displaying the revealed letters in the word. Ensures that the lengths are the same
def set_reveal_list():
    for space in range(len(comp_word)):
        reveal_list.append("-")

def modify_reveal_list(space, guess):
    reveal_list[space] = guess

def modify_guessed_letters(guess):
    guessed_letters.append(guess)

def check():
    if reveal_list == comp_word_list:
        return True

for char in comp_word:
    comp_word_list.append(char)

    
set_reveal_list()

print(reveal_list)
print(comp_word)
print(comp_word_list)

print(f"Welcome to Hangman! You get a total of {num_guesses} incorrect guesses before you lose...\nDuplicate guesses do not count! Good luck")

while num_guesses > 0 and game_won == False:
    correct = False
    print(f"Number of guesses left: {num_guesses}")
    user_guess = input("Guess a letter: ").lower()
    
    for char in comp_word_list:
        if user_guess == comp_word_list[char]:
            correct = True
            reveal_list[char] = user_guess
            if user_guess not in guessed_letters:
                guessed_letters.append(user_guess)

    if correct == False:
        print("{user_guess} is not in this word...")
        num_guesses -= 1
        if user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
    
    if check() == True:
        break

if num_guesses == 0 and game_won == False:
    print("You Lose!")
else:
    print("You Win!")