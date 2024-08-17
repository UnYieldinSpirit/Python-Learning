import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

payer = friends[random.randint(0, 4)]

print(f"The person that has to pay is: {payer}! Sorry not sorry!")

# -------------------------OR----------------------------

print(random.choice(friends)) # chooses a random item in the list, no need to try and identify the parameters that are needed in randint()