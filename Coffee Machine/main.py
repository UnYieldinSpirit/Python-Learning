MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

inserted_coins = {
    "quarter": 0,
    "dime": 0,
    "nickel": 0,
    "penny": 0,
}

profit = 0

def user_drink_check():
    """ensures the user's inputs for drinks are valid"""
    user = input("What would you like? (latte/ cappuccino/ espresso) ").lower()
    if user != 'latte' and user != 'cappuccino' and user != 'espresso' and user != 'report':
        print("That is not a valid choice")
        user = user_drink_check()
        return user
    else:
        return user

def user_coin_check(coin):
    """ensures the user's inputs for coins are valid"""
    if coin == "penny":
        user = input(f"How many pennies:")
    else:
        user = input(f"How many {coin}s:")

    if user.type() != int:
        print("That is not a valid input")
        user = user_coin_check(coin)
        return user
    else:
        return user

def calculate_change(customer_payment, drink):
    """returns the change based on what the customer ordered and paid"""
    change = customer_payment - MENU[drink]['cost']
    return change

def reduce_resources(drink):
    """reduces the remaining resources in the coffee machine based on the selected drink"""
    print(resources)
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
    print(resources)
    
def print_resources():
    """prints the remaining resources in the coffee machine"""
    for i in resources:
        if i == "coffee":
            print(f"{i}: {resources[i]}g")
        else:
            print(f"{i}: {resources[i]}ml")            
    print(f"Money: ${profit}")

def ask_coins():
    print("test")

# TODO - 1. finish ask_coins() function
# TODO - 2. begin the implementation of the functions into the main logical handling function
# TODO - 3. delete the blah.py that is used as a holder program
# TODO - 4. remove the tempCodeRunnerFile.py