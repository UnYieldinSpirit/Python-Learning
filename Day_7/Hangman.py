import random

word_bank = ["peanut", "alphabet", "caramel", "gideon", "flabbergasted"]
comp_word = random.choice(word_bank)
comp_word_list = []
reveal_list = []
guessed_letters = []
num_guesses = 5
correct = False # variable that tracks if the user's guess is correct

# function that sets the list that handles displaying the revealed letters in the word. Ensures that the lengths are the same
def set_reveal_list():
    for space in range(len(comp_word)):
        reveal_list.append("-")

def modify_reveal_list(space, guess):
    reveal_list[space] = guess

def modify_guessed_letters(guess):
    guessed_letters.append(guess)

for char in comp_word:
    comp_word_list.append(char)
    
set_reveal_list()

print(reveal_list)
print(comp_word)
print(comp_word_list)

print(f"Welcome to Hangman! You get a total of {num_guesses} incorrect guesses before you lose...\nDuplicate guesses do not count! Good luck")

while(num_guesses > 0 and correct == False):
    correct = False
    print(f"Number of guesses left: {num_guesses}")


    num_guesses -= 1