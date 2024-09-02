import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # infinite deck, meaning that when a card is drawn, it is not removed from the card pool
hands = {
    "player": [],
    "computer": [],
}

def p_deal(first_deal):
    if first_deal == True:
        hands["player"].append(random.choice(cards))   
    hands["player"].append(random.choice(cards))
    print("Player:")
    print(hands["player"])

def comp_deal(first_deal):
    if first_deal == True:
        hands["computer"].append(random.choice(cards))
    hands["computer"].append(random.choice(cards))
    print("Computer:")
    print(hands["computer"])

def initiate_game():
    first_deal = True
    print("""Welcome to the BlackJack Table. The goal is to get as close as you can to 21 without exceeding. May the heart of the cards be with you.
          Aces are 11 or 1, depending on if you are over 21 or not.
          All face cards equal 10
          The number cards are just number cards
          """)
    hands["computer"] = []
    hands["player"] = []
    comp_deal(first_deal)
    p_deal(first_deal)

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
        return True
    else:
        return False

def user_choice():
    user = input("'Hit' (h) or 'Stand' (s)? ").lower()
    if "s" != user != "h":
        print("That is not a valid choice")
        user = user_choice()
        return user
    else:
        return user

def total(name):
    total = 0
    for char in hands[name]:
        total += char
    return total

p_over_21 = False
comp_over_21 = False
initiate_game()
while p_over_21 == False and comp_over_21 == False:
    user = user_choice()
    if user == "h":
        p_deal(False)
        comp_deal(False)
        p_over_21 = check("player")
        comp_over_21 = check("computer")
    elif user == "s":
        while total("computer") < total("player") and comp_over_21 == False:
            print("Player:")
            print(hands["player"])
            comp_deal(False)
            p_over_21 = check("player")
            comp_over_21 = check("computer")

if comp_over_21 == True and p_over_21 == False:
    print("You Win!")
elif comp_over_21 == True and p_over_21 == True:
    print("You Lose!")
elif comp_over_21 == False and p_over_21 == True:
    print("You Lose!")

# Need to make it so that if you stand, you can not continue hitting or standing