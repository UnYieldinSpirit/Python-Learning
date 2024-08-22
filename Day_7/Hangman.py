import random

word_bank = ["peanut", "alphabet", "caramel", "gideon", "flabbergasted"]
comp_word = random.choice(word_bank)
num_guesses = 5

print(comp_word)

print(f"Welcome to Hangman! You get a total of {num_guesses} guesses before you lose...\nDuplicate guesses do not count! Good luck")

while(num_guesses > 0):
    print(f"Number of guesses left: {num_guesses}")
    num_guesses -= 1