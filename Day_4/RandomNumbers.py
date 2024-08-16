import random # imports the random module so that we can use the module and all of its inclusions

random_integer = random.randint(1, 50)
print(random_integer)

random_number_0_to_1 = random.random() * 100 # multiplying by a number greatly extends the range of the randomization
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)