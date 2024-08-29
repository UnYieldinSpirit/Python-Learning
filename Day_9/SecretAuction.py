import AuctionGavel

# program used to conduct a secret auction

print(AuctionGavel.logo)
print("Welcome to the Secret Auction!")

auctions = {}

def auction_inputs(dict, key, value):
     dict[key] = value

def calculate_winner(dict):
     top_bid = 0
     top_bidder = ""

     for key in dict:
        if dict[key] > top_bid: # compares each bid with the current top bid and sets the higher of the two as the top bid
             top_bid = dict[key]
             top_bidder = key

     print(f"The winner with the highest bid of ${dict[top_bidder]}, is {top_bidder}!")
              
def clear(): # artificial clear of the terminal
     print("\n" *100)

proceed = True

while proceed == True: # coninues the loop until no more entries are entered
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_inputs(auctions, name, bid)
    answer = input("Are there any more bidders? (y/n) ")

    if answer == 'y':
         clear()
    else:
         proceed = False

calculate_winner(auctions)