import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

win = "You Win!"
lose = "You Lose..."
tie = "You Tied. Try again!"

choices = [rock, paper, scissors]

# player_choice = int(input("Welcome to Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

play_again = True

while play_again == True:
    play_again = True

    # two variables used to determine if the user is entering in valid choices
    x = True
    y = True
    draw = True

    while draw == True:
        while x == True:
            try:
                while y == True:
                    player_choice = int(input("Welcome to Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
                    if player_choice >= 3 or player_choice < 0:
                        print("That's not a valid number... Try again")
                    else:
                        y = False
                        x = False
            except ValueError:
                print("That's not a valid number. Try again")

        print(choices[player_choice])

        computer_choice = random.randint(0, 2)

        print(f"Computer chose:\n{choices[computer_choice]}")

        # logic: 0 < 1 < 2 < 0
        if player_choice == computer_choice:
            print(tie)
        elif player_choice == 0 and computer_choice == 2:
            print(win)
            draw = False
        elif player_choice == 2 and computer_choice == 0:
            print(lose)
            draw = False
        elif player_choice < computer_choice:
            print(lose)
            draw = False
        else:
            print(win)
            draw = False
    play_question = input("Play Again? 'y/n?': ").lower()

    if play_question == "n":
        play_again = False
    else:
        play_again = True