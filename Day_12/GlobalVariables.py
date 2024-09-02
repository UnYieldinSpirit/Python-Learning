enemies = 1

def increase_enemies(enemy): # instead of modifying the global scope of the variable, it could be better practice to just return the variable output
    print(f"enemies inside the function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside of the funtion: {enemies}")