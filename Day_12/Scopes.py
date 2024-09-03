enemies = 1 # one variable

def increase_enemies():
    enemies = 2 # a new variable is created, the original enemies is not touched or modified
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside of the function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2 # variables are only accessible in the walls of the function
    print(potion_strength)

drink_potion()

# Global Scope
player_health = 10 # declared outside of function, so it is accessible by all functions


def drink_potion_global():
    potion_strength = 2
    print(player_health)

def game():
    def attack():
        damage = 2
        player_health -= damage
        print("Player has taken {damage} damage")
    attack()

game()
