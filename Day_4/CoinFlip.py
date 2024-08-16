import random

# Print heads or tails
coin_outcome = random.randint(0,1) # heads = 0, tails = 1

if coin_outcome == 0:
    outcome = "Heads"
else:
    outcome = "Tails"

print(f"You flip a coin, and the result is:\n{outcome}!")