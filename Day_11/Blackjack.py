import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # infinite deck, meaning that when a card is drawn, it is not removed from the card pool
hands = {
    "player": [3, 5, 6, 10],
    "computer": [],
}

# count = 0
# for char in "alphabet":
#     hands["player"].append(cards[count])
#     count += 1

# print(dict)

# counter = 0
# for char in "goop":
#     print(hands["player"][counter])
#     counter += 1

def p_deal():
    hands["player"].append(random.choice(cards))
    print("Player:")
    print(hands["player"])

def comp_deal():
    hands["computer"].append(random.choice(cards))
    print("Computer:")
    print(hands["computer"])

def initiate_game():
    print("""Welcome to the BlackJack Table. The goal is to get as close as you can to 21 without exceeding. May the heart of the cards be with you.
          Aces are 11 or 1, depending on if you are over 21 or not.
          All face cards equal 10
          The number cards are just number cards
          """)
    comp_deal()
    p_deal()
    
def check(name):
    total = 0
    for char in hands[name]:
        total += char
    if total > 21:
        return True



p_over_21 = False
comp_over_21 = False

initiate_game()
# while p_under_21 == False and comp_under_21 == False: