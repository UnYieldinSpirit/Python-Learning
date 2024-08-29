import AuctionGavel

# program used to conduct a secret auction

print(AuctionGavel.logo)
print("Welcome to the Secret Auction!")

auctions = {}

def auction_inputs(dict, key, value):
     dict[key] = value
     return

def calculate_winner(dict):
     print(dict)

def clear():
     print("\n" *100)

proceed = True

while proceed == True:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    auction_inputs(auctions, name, bid)
    answer = input("Are there any more bidders? (y/n) ")
    if answer == 'y':
         clear()
    else:
         proceed = False

calculate_winner(auctions)