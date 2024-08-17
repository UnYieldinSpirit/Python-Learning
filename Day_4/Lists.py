states_of_america = ["Delaware", "Pennsylvania", "Maryland", "Wisconsin"] # order is also saved

print(states_of_america[0]) # first item is at the 0 location

states_of_america[3] = "Connecticut" # can alter any index

print(states_of_america[3])

states_of_america.append("West Virginia") # adds an item to the end of the 

print(states_of_america[4])

fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Lemons", "Limes"]
vegetables = ["Carrots", "Kale", "Watermelon", "Collard Greens","Broccoli"]

edible = [fruits, vegetables]

print(edible[1][3]) # should print the 4th item in the 2nd list