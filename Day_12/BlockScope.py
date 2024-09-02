game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy(): # variables created within a function can only be accessed in the function
    new_enemy = ""
    if game_level < 5: 
        new_enemy = enemies[0] # variables created in conditional blocks can be accessed anywhere

    print(new_enemy)