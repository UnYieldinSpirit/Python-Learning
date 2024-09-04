import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # infinite deck, meaning that when a card is drawn, it is not removed from the card pool
new_cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,]
hands = {
    "player": [],
    "computer": [],
}

greeting = """Welcome to the BlackJack Table. The goal is to get as close as you can to 21 without exceeding. May the heart of the cards be with you.
Aces are 11 or 1, depending on if you are over 21 or not.
All face cards equal 10
The number cards are just number cards
          """

def total(name):
    total = 0
    for char in hands[name]:
        total += char
    return total

def p_deal(first_deal):
    if first_deal == True:
        hands["player"].append(random.choice(cards))   
    hands["player"].append(random.choice(cards))
    if first_deal:
        print("Player:")
        print(f"{hands['player']} Total = {total('player')}")

def comp_deal(first_deal):
    if first_deal == True:
        hands["computer"].append(random.choice(cards))
    hands["computer"].append(random.choice(cards))
    if first_deal:
        print("Computer:")
        print(f"{hands['computer']}  Total = {total('computer')}")

def initiate_game():
    first_deal = True
    print(greeting)
    hands["computer"] = []
    hands["player"] = []
    p_deal(first_deal)
    comp_deal(first_deal)

def ace_convert(name): # used to change any number whose value is 11 to 1 if over 21
    index = hands[name].index(11)
    hands[name][index] = 1
    
def check(name):
    """Checks the value of the hand in order to determine if it is over 21 or not"""
    total = 0
    for char in hands[name]:
        total += char
    while total > 21 and 11 in hands[name]:
        total -= 10
        ace_convert(name)
    if total > 21:
        print(f"{name}:")
        print(f"{hands[name]}  Total = {total}")
        return True
    else:
        print(f"{name}:")
        print(f"{hands[name]}  Total = {total}")
        return False

def user_choice():
    user = input("'Hit' (h) or 'Stand' (s)? ").lower()
    if "s" != user != "h":
        print("That is not a valid choice")
        user = user_choice()
        return user
    else:
        return user

def declare_winner():
    player = total("player")
    computer = total("computer")
    if computer > player:
        print("You Lose!")
    elif computer == player:
        print("You Lose! The House Always Wins!")
    end = True
    return end

game_over = False
p_over_21 = False
comp_over_21 = False
comp_win = False

initiate_game()
while (p_over_21 == False and comp_over_21 == False) and not game_over:
    user = user_choice()
    if user == "h":
        p_deal(False)
        if total("computer") < 18:
            comp_deal(False)
        p_over_21 = check("player")
        comp_over_21 = check("computer")
    elif user == "s":
        while (total("computer") <= total("player")) and total("computer") < 21:
            comp_deal(False)
            p_over_21 = check("player")
            comp_over_21 = check("computer")
        if not p_over_21 and not comp_over_21:
            game_over = declare_winner()

if comp_over_21 == True and p_over_21 == False:
    print("You Win!")
elif comp_over_21 == True and p_over_21 == True:
    print("Draw! You Lose! The House ALWAYS Wins!")
elif comp_over_21 == False and p_over_21 == True:
    print("BUST! You Lose!")

print("Thank you for playing!")

# adding the capability to take cards out that have been drawn is not hard at all. Track the drawn number and index to remove